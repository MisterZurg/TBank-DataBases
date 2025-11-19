# Сохранённая версия

import argparse
import json
import os
import sys
from pathlib import Path
from typing import List, Any

import psycopg2
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configuration
DB_DSN = {
    "dbname": os.getenv("DB_NAME", "testdb"),
    "user": os.getenv("DB_USER", "test"),
    "password": os.getenv("DB_PASSWORD", "test"),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", 5432)),
}

BASE_DIR = Path(__file__).parent
TEST_SUITE_FILE = BASE_DIR / "tests.json"
SOLUTIONS_DIR = BASE_DIR / "student_solutions"
SOLUTIONS_DIR.mkdir(exist_ok=True)


# Helper functions
def execute_sql(conn, query: str) -> List[Any]:
    """Execute SQL and return results"""
    if not query or not query.strip():
        return []
    with conn.cursor() as cur:
        cur.execute(query)
        if cur.description:
            return cur.fetchall()
        conn.commit()
        return []


def normalize_rows(rows):
    """Normalize rows for comparison"""
    if rows is None:
        return []
    from datetime import date
    from decimal import Decimal

    norm = []
    for r in rows:
        row = []
        for v in r:
            if isinstance(v, date):
                row.append(v.isoformat())
            elif isinstance(v, Decimal):
                row.append(float(v))
            else:
                row.append(v)
        norm.append(row)
    return norm


def fill_template(template: str, params: dict) -> str:
    """Fill template with parameters"""
    stmt = template
    for k, v in params.items():
        placeholder = "{{" + k + "}}"
        if isinstance(v, str):
            if v.startswith("'") and v.endswith("'"):
                replacement = v
            else:
                replacement = "'" + v.replace("'", "''") + "'"
        elif v is None:
            replacement = "NULL"
        else:
            replacement = str(v)
        stmt = stmt.replace(placeholder, replacement)
    return stmt


def load_test_suite():
    with open(TEST_SUITE_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def find_test(test_suite, test_id):
    test = next((t for t in test_suite['tests'] if t['test_id'] == test_id), None)
    if not test:
        raise ValueError("Test not found")
    return test


def find_case(test, case_id):
    case = next((c for c in test['cases'] if c['case_id'] == case_id), None)
    if not case:
        raise ValueError("Case not found")
    return case


def run_cli_mode():
    """Запуск всех тестов в консольном режиме"""
    test_suite = load_test_suite()
    results = [execute_test_logic(test_suite, t) for t in test_suite['tests']]

    passed = sum(1 for r in results if r['status'] == 'passed')
    failed = len(results) - passed

    print("\n=== SQL Test Runner CLI ===\n")
    for r in results:
        print(f"Test {r['test_id']} ({r['alias']}): {r['status']}")
        for c in r['cases']:
            status = c['status']
            print(f"  Case {c['case_id']}: {status}")
            if status == "failed":
                print(f"    Expected: {c.get('expected')}")
                print(f"    Actual:   {c.get('actual')}")
            for chk in c.get("checks", []):
                chk_status = chk.get("status")
                print(f"    Check {chk['check_id']}: {chk_status}")
                if chk_status != "passed":
                    print(f"      SQL: {chk['check_sql']}")
                    print(f"      Expected: {chk.get('check_expected')}")
                    print(f"      Actual: {chk.get('actual', chk.get('error'))}")
        print()
    print(f"Total: {len(results)} tests, Passed: {passed}, Failed: {failed}")
    return failed == 0


# API Endpoints

@app.route('/')
def index():
    """API documentation"""
    return jsonify({
        "name": "SQL Test Runner API",
        "version": "2.0",
        "endpoints": {
            "/api/test-suite": "GET - Load test suite",
            "/api/results": "GET - Get all test results",
            "/api/solution/<test_id>": "GET - Load solution, POST - Save solution",
            "/api/run-test/<test_id>": "POST - Run specific test",
            "/api/run-case/<test_id>/<case_id>": "POST - Run specific case",
            "/api/run-all": "POST - Run all tests",
            "/api/reload": "POST - Reload from files"
        }
    })


@app.route('/api/test-suite', methods=['GET'])
def get_test_suite():
    """Load test suite from file"""
    try:
        if not TEST_SUITE_FILE.exists():
            return jsonify({"error": "Test suite file not found"}), 404

        with open(TEST_SUITE_FILE, 'r', encoding='utf-8') as f:
            test_suite = json.load(f)

        return jsonify(test_suite)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def execute_test_logic(test_suite, test, case=None):
    """Общая логика выполнения теста или кейса с проверками"""
    alias = test['alias']
    solution_file = SOLUTIONS_DIR / f"{test['test_id']}_{alias}.sql"

    if not solution_file.exists():
        raise FileNotFoundError("Solution file not found")

    student_sql = solution_file.read_text(encoding='utf-8').strip()

    conn = psycopg2.connect(**DB_DSN)
    conn.autocommit = True

    results = []
    passed_cases = 0
    failed_cases = 0
    all_checks = test['checks']

    try:
        # Setup
        if test_suite.get('setup'):
            execute_sql(conn, test_suite['setup'])

        # Выбираем кейсы: один или все
        cases = [case] if case else test['cases']

        for c in cases:
            # Cleanup перед кейсом
            if test_suite.get('cleanup'):
                execute_sql(conn, test_suite['cleanup'])

            # Подготовка данных
            params = c.get('params', {})
            for template in test.get('data_templates', []):
                stmt = fill_template(template, params)
                execute_sql(conn, stmt)

            # Выполнение решения студента
            try:
                actual = execute_sql(conn, student_sql)
                actual_norm = normalize_rows(actual)
                expected_norm = normalize_rows(c.get('expected', []))

                order_matters = test.get('order_matters', False)
                passed = (
                    actual_norm == expected_norm
                    if order_matters
                    else sorted(actual_norm) == sorted(expected_norm)
                )

                if passed:
                    passed_cases += 1
                else:
                    failed_cases += 1

                case_result = {
                    **c,
                    "status": "passed" if passed else "failed",
                    "actual": actual_norm
                }

            except Exception as e:
                failed_cases += 1
                case_result = {
                    **c,
                    "status": "failed",
                    "actual": [],
                    "error": str(e)
                }

            # --- Выполнение проверок ---
            case_checks = []
            for chk in c.get("checks", []):
                try:
                    check_result = execute_sql(conn, chk["check_sql"])
                    check_norm = normalize_rows(check_result)

                    expected_type = chk["check_expected"]["type"]

                    if expected_type == "value":
                        expected_value = chk["check_expected"]["value"]
                        passed_check = (
                                bool(check_norm)
                                and check_norm[0][0] == expected_value
                        )

                    elif expected_type == "columns":
                        expected_cols = chk["check_expected"]["columns"]
                        actual_cols = [{"name": r[0], "type": r[1]} for r in check_norm]
                        passed_check = actual_cols == expected_cols

                    elif expected_type == "rows":
                        # Сравниваем все строки целиком
                        expected_rows = chk["check_expected"]["rows"]
                        # Приводим обе стороны к списку списков для надёжного сравнения
                        actual_rows = [list(row) for row in check_norm]
                        passed_check = actual_rows == expected_rows

                    else:
                        passed_check = False  # неизвестный тип проверки

                    case_checks.append({
                        **chk,
                        "status": "passed" if passed_check else "failed",
                        "actual": check_norm
                    })

                except Exception as e:
                    case_checks.append({
                        **chk,
                        "status": "error",
                        "error": str(e)
                    })

                except Exception as e:
                    case_checks.append({
                        **chk,
                        "status": "failed",
                        "actual": [],
                        "error": str(e)
                    })

            if any(chk["status"] in ("failed", "error") for chk in case_checks):
                case_result["status"] = "failed"

            case_result["checks"] = case_checks
            results.append(case_result)

        # Cleanup после теста
        if test_suite.get('cleanup'):
            execute_sql(conn, test_suite['cleanup'])

    finally:
        conn.close()

    status = "passed" if failed_cases == 0 else "failed"

    return {
        "test_id": test['test_id'],
        "alias": alias,
        "status": status,
        "total_cases": len(cases),
        "passed_cases": passed_cases,
        "failed_cases": failed_cases,
        "cases": results,
        "checks": all_checks,
        "student_solution": student_sql
    }


@app.route('/api/solution/<test_id>', methods=['GET', 'POST'])
def handle_solution(test_id):
    """Load or save student solution"""
    try:
        # Find test alias
        with open(TEST_SUITE_FILE, 'r', encoding='utf-8') as f:
            test_suite = json.load(f)

        test = next((t for t in test_suite['tests'] if t['test_id'] == test_id), None)
        if not test:
            return jsonify({"error": "Test not found"}), 404

        alias = test['alias']
        solution_file = SOLUTIONS_DIR / f"{test_id}_{alias}.sql"

        if request.method == 'GET':
            # Load solution from file
            if solution_file.exists():
                solution = solution_file.read_text(encoding='utf-8')
            else:
                solution = f"-- Напишите ваше решение для теста {test_id}\n-- {alias}\n\n"

            return jsonify({"solution": solution})

        elif request.method == 'POST':
            # Save solution to file
            data = request.json
            solution = data.get('solution', '')

            solution_file.write_text(solution, encoding='utf-8')

            return jsonify({"success": True, "message": "Solution saved"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/run-test/<test_id>', methods=['POST'])
def run_test(test_id):
    try:
        test_suite = load_test_suite()
        test = find_test(test_suite, test_id)
        result = execute_test_logic(test_suite, test)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/run-case/<test_id>/<case_id>', methods=['POST'])
def run_case(test_id, case_id):
    try:
        test_suite = load_test_suite()
        test = find_test(test_suite, test_id)
        case = find_case(test, case_id)
        result = execute_test_logic(test_suite, test, case)
        return jsonify(result["cases"][0])  # возвращаем один кейс
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/run-all', methods=['POST'])
def run_all_tests():
    try:
        test_suite = load_test_suite()
        results = [execute_test_logic(test_suite, t) for t in test_suite['tests']]

        passed = sum(1 for r in results if r['status'] == 'passed')
        failed = len(results) - passed

        return jsonify({
            "meta": test_suite.get('meta', {}),
            "success": failed == 0,
            "total_tests": len(results),
            "passed_tests": passed,
            "failed_tests": failed,
            "results": results
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/reload', methods=['POST'])
def reload_from_files():
    """Reload test suite and solutions from files"""
    try:
        # Just return success - files are always read fresh
        return jsonify({"success": True, "message": "Reloaded from files"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="SQL Test Runner")
    parser.add_argument('--cli', action='store_true', help="Run all tests in CLI mode")
    parser.add_argument('--port', type=int, default=int(os.getenv('PORT', 5001)), help="API server port")
    parser.add_argument('--host', type=str, default='0.0.0.0', help="API server host")
    args = parser.parse_args()

    if args.cli:
        success = run_cli_mode()
        sys.exit(0 if success else 1)
    else:
        print("🚀 SQL Test Runner API Server")
        print(f"📁 Test suite: {TEST_SUITE_FILE}")
        print(f"📁 Solutions: {SOLUTIONS_DIR}")
        print(f"🗄️  Database: {DB_DSN['dbname']}@{DB_DSN['host']}:{DB_DSN['port']}")
        print(f"🌐 Server: http://{args.host}:{args.port}")
        app.run(debug=True, host=args.host, port=args.port)

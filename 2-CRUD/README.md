# Тест 2 Основы запросов: CRUD и фильтрация
1. Что означает аббревиатура CRUD?

- Create, Read, Update, Delete


2. Какой SQL-оператор используется для добавления новых строк в таблицу?

```sql
INSERT INTO
```

3. Какой тип данных лучше использовать для хранения роста?

```sql
INT
```

4. Какие типы данных относятся к строковым?

```sql
VARCHAR

TEXT

CHAR
```

5. Что делает оператор `DELETE FROM students WHERE id = 3;`?

- Удаляет только запись с `id = 3`

6. Какой оператор используется для изменения существующих данных?

```sql
UPDATE
```

7. Какой запрос выберет всех студентов старше 18 лет?

```sql
SELECT * FROM students WHERE age > 18;
```

8. Какой запрос корректно добавляет студента Алина Смирнова (19 лет, alina@mail.ru)

```sql
INSERT INTO students VALUES ('Алина','Смирнова',19,'alina@mail.ru');
```

9. Как обновить email студента с `id = 2` на `new@mail.com`?

```sql
UPDATE students SET email = 'new@mail.com' WHERE id = 2;
```

10. Что делает оператор `BETWEEN 10 AND 20`?

- Проверяет, входит ли значение в диапазон от 10 до 20


11. Соотнесите тип данных и пример значения:

- 'two'
- '26-september-of-2025'

Решение
``` 
INT 42
VARCHAR 'Привет' -- 'two', '26-september-of-2025'
BOOLEAN true
DATE '2025-10-26'
```

12. Какой тип данных позволяет хранить вложенные объекты (полуструктурированные данные)?

```sql
JSONB
```

13. Как удалить всех студентов младше 18 лет?

```sql
DELETE FROM students WHERE age < 18;
```

14. Какой порядок выполнения логических операторов верный?

```sql
NOT > AND > OR
```

15. Какие выражения вернут true для строки `'Ivan' LIKE ...`?

- `'Ivan' LIKE 'I%'`
- `'Ivan' LIKE '%n'`
- `'Ivan' LIKE 'Iv_n'`


16. Какой результат вернёт выражение `age BETWEEN 18 AND 25` при `age = 17`?

```sql
FALSE
```

17. Какой запрос корректно создаёт таблицу `courses`?

```sql
CREATE TABLE courses (id SERIAL PRIMARY KEY, name VARCHAR(100), hours INT);
```


18. Какой запрос вернёт только фамилии всех студентов?

```sql
SELECT * FROM students;

SELECT last_name FROM students;
```

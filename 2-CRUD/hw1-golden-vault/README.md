# Задания для студентов

## SQL тесты на CRUD операции для Золотого хранилища Т-Банка

### ⚙️ Инициализация базы данных
```sql
CREATE TABLE IF NOT EXISTS clients (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100),
    passport_number VARCHAR(20),
    created_at DATE
);

CREATE TABLE IF NOT EXISTS vaults (
    id SERIAL PRIMARY KEY,
    vault_name VARCHAR(50),
    capacity_g DECIMAL,
    location VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS gold_deposits (
    id SERIAL PRIMARY KEY,
    client_id INT ,
    vault_id INT,
    weight_g DECIMAL,
    deposit_date DATE
);
```

### 🧹 Очистка между кейсами
```sql
TRUNCATE gold_deposits, vaults, clients RESTART IDENTITY;
```

### 💣 Полный сброс базы данных
```sql
DROP TABLE IF EXISTS gold_deposits, vaults, clients;
```

---

## Задание 001: Выбрать имя и номер паспорта всех клиентов

**Тип:** `select`  
**Сложность:** 1/3  

📝 Файл для решения: [`student_solutions/001_select_client_name_passport.sql`](student_solutions/001_select_client_name_passport.sql)

### Пример данных для отображения:
```json
{
  "clients": {
    "columns": [
      "id",
      "full_name",
      "passport_number",
      "created_at"
    ],
    "rows": [
      [
        134,
        "Лора",
        "803875561033",
        null
      ]
    ]
  },
  "vaults": {
    "columns": [
      "id",
      "vault_name",
      "capacity_g",
      "location"
    ],
    "rows": []
  },
  "gold_deposits": {
    "columns": [
      "id",
      "client_id",
      "vault_id",
      "weight_g",
      "deposit_date"
    ],
    "rows": []
  }
}
```

---

## Задание 002: Выбрать названия всех хранилищ и их вместимость

**Тип:** `select`  
**Сложность:** 1/3  

📝 Файл для решения: [`student_solutions/002_select_vault_name_capacity.sql`](student_solutions/002_select_vault_name_capacity.sql)

### Пример данных для отображения:
```json
{
  "clients": {
    "columns": [
      "id",
      "full_name",
      "passport_number",
      "created_at"
    ],
    "rows": []
  },
  "vaults": {
    "columns": [
      "id",
      "vault_name",
      "capacity_g",
      "location"
    ],
    "rows": [
      [
        336,
        "cdaNUC",
        517.79,
        null
      ]
    ]
  },
  "gold_deposits": {
    "columns": [
      "id",
      "client_id",
      "vault_id",
      "weight_g",
      "deposit_date"
    ],
    "rows": []
  }
}
```

---

## Задание 003: Выбрать все депозиты, где вес золота больше 500 грамм

**Тип:** `select`  
**Сложность:** 1/3  

📝 Файл для решения: [`student_solutions/003_select_gold_deposits_filter.sql`](student_solutions/003_select_gold_deposits_filter.sql)

### Пример данных для отображения:
```json
{
  "clients": {
    "columns": [
      "id",
      "full_name",
      "passport_number",
      "created_at"
    ],
    "rows": [
      [
        349,
        "Радим",
        "800975661324",
        null
      ]
    ]
  },
  "vaults": {
    "columns": [
      "id",
      "vault_name",
      "capacity_g",
      "location"
    ],
    "rows": [
      [
        187,
        "jrboHw",
        320.67,
        null
      ]
    ]
  },
  "gold_deposits": {
    "columns": [
      "id",
      "client_id",
      "vault_id",
      "weight_g",
      "deposit_date"
    ],
    "rows": [
      [
        1,
        349,
        187,
        402.38,
        "2012-02-26"
      ]
    ]
  }
}
```

---

## Задание 004: Добавить нового клиента

**Тип:** `insert`  
**Сложность:** 1/3  

📝 Файл для решения: [`student_solutions/004_insert_client.sql`](student_solutions/004_insert_client.sql)

### Пример данных для отображения:
```json
{
  "clients": {
    "columns": [
      "id",
      "full_name",
      "passport_number",
      "created_at"
    ],
    "rows": [
      [
        171,
        "Аскольд",
        "345050900854",
        null
      ],
      [
        1,
        "Иван Иванов",
        "4500 123456",
        null
      ]
    ]
  },
  "vaults": {
    "columns": [
      "id",
      "vault_name",
      "capacity_g",
      "location"
    ],
    "rows": []
  },
  "gold_deposits": {
    "columns": [
      "id",
      "client_id",
      "vault_id",
      "weight_g",
      "deposit_date"
    ],
    "rows": []
  }
}
```

---

## Задание 005: Добавить новое хранилище

**Тип:** `insert`  
**Сложность:** 1/3  

📝 Файл для решения: [`student_solutions/005_insert_vault.sql`](student_solutions/005_insert_vault.sql)

### Пример данных для отображения:
```json
{
  "clients": {
    "columns": [
      "id",
      "full_name",
      "passport_number",
      "created_at"
    ],
    "rows": []
  },
  "vaults": {
    "columns": [
      "id",
      "vault_name",
      "capacity_g",
      "location"
    ],
    "rows": [
      [
        943,
        "LAKBwA",
        910.98,
        null
      ],
      [
        1,
        "Хранилище A",
        10000.0,
        null
      ]
    ]
  },
  "gold_deposits": {
    "columns": [
      "id",
      "client_id",
      "vault_id",
      "weight_g",
      "deposit_date"
    ],
    "rows": []
  }
}
```

---

## Задание 006: Добавить новый депозит

**Тип:** `insert`  
**Сложность:** 1/3  

📝 Файл для решения: [`student_solutions/006_insert_gold_deposit.sql`](student_solutions/006_insert_gold_deposit.sql)

### Пример данных для отображения:
```json
{
  "clients": {
    "columns": [
      "id",
      "full_name",
      "passport_number",
      "created_at"
    ],
    "rows": []
  },
  "vaults": {
    "columns": [
      "id",
      "vault_name",
      "capacity_g",
      "location"
    ],
    "rows": []
  },
  "gold_deposits": {
    "columns": [
      "id",
      "client_id",
      "vault_id",
      "weight_g",
      "deposit_date"
    ],
    "rows": [
      [
        77,
        132,
        535,
        575.67,
        "1999-12-25"
      ],
      [
        1,
        1,
        1,
        750.0,
        "2025-11-01"
      ]
    ]
  }
}
```

---

## Задание 007: Обновить номер паспорта клиента

**Тип:** `update`  
**Сложность:** 1/3  

📝 Файл для решения: [`student_solutions/007_update_client_passport.sql`](student_solutions/007_update_client_passport.sql)

### Пример данных для отображения:
```json
{
  "clients": {
    "columns": [
      "id",
      "full_name",
      "passport_number",
      "created_at"
    ],
    "rows": [
      [
        1,
        "Агафон",
        "4500 654321",
        null
      ]
    ]
  },
  "vaults": {
    "columns": [
      "id",
      "vault_name",
      "capacity_g",
      "location"
    ],
    "rows": []
  },
  "gold_deposits": {
    "columns": [
      "id",
      "client_id",
      "vault_id",
      "weight_g",
      "deposit_date"
    ],
    "rows": []
  }
}
```

---

## Задание 008: Удалить депозит клиента

**Тип:** `delete`  
**Сложность:** 1/3  

📝 Файл для решения: [`student_solutions/008_delete_deposit.sql`](student_solutions/008_delete_deposit.sql)

### Пример данных для отображения:
```json
{
  "clients": {
    "columns": [
      "id",
      "full_name",
      "passport_number",
      "created_at"
    ],
    "rows": []
  },
  "vaults": {
    "columns": [
      "id",
      "vault_name",
      "capacity_g",
      "location"
    ],
    "rows": []
  },
  "gold_deposits": {
    "columns": [
      "id",
      "client_id",
      "vault_id",
      "weight_g",
      "deposit_date"
    ],
    "rows": []
  }
}
```

---

## Задание 009: Посчитать общий вес золота в каждом хранилище

**Тип:** `select`  
**Сложность:** 1/3  

📝 Файл для решения: [`student_solutions/009_select_total_gold_per_vault.sql`](student_solutions/009_select_total_gold_per_vault.sql)

### Пример данных для отображения:
```json
{
  "clients": {
    "columns": [
      "id",
      "full_name",
      "passport_number",
      "created_at"
    ],
    "rows": []
  },
  "vaults": {
    "columns": [
      "id",
      "vault_name",
      "capacity_g",
      "location"
    ],
    "rows": [
      [
        987,
        "oFiimTSK",
        685.0,
        null
      ]
    ]
  },
  "gold_deposits": {
    "columns": [
      "id",
      "client_id",
      "vault_id",
      "weight_g",
      "deposit_date"
    ],
    "rows": [
      [
        313,
        932,
        987,
        162.7,
        "2019-10-06"
      ]
    ]
  }
}
```

---

## Задание 010: Выбрать имя клиента и вес его депозитов

**Тип:** `select`  
**Сложность:** 1/3  

📝 Файл для решения: [`student_solutions/010_select_client_deposits_join.sql`](student_solutions/010_select_client_deposits_join.sql)

### Пример данных для отображения:
```json
{
  "clients": {
    "columns": [
      "id",
      "full_name",
      "passport_number",
      "created_at"
    ],
    "rows": [
      [
        330,
        "Лаврентий",
        "363750635602",
        null
      ]
    ]
  },
  "vaults": {
    "columns": [
      "id",
      "vault_name",
      "capacity_g",
      "location"
    ],
    "rows": []
  },
  "gold_deposits": {
    "columns": [
      "id",
      "client_id",
      "vault_id",
      "weight_g",
      "deposit_date"
    ],
    "rows": [
      [
        894,
        330,
        998,
        582.4,
        "2024-02-24"
      ]
    ]
  }
}
```

---

## Задание 011: Обновить вместимость хранилища

**Тип:** `update`  
**Сложность:** 1/3  

📝 Файл для решения: [`student_solutions/011_update_vault_capacity.sql`](student_solutions/011_update_vault_capacity.sql)

### Пример данных для отображения:
```json
{
  "clients": {
    "columns": [
      "id",
      "full_name",
      "passport_number",
      "created_at"
    ],
    "rows": []
  },
  "vaults": {
    "columns": [
      "id",
      "vault_name",
      "capacity_g",
      "location"
    ],
    "rows": [
      [
        1,
        "CvOdNv",
        15000.0,
        null
      ]
    ]
  },
  "gold_deposits": {
    "columns": [
      "id",
      "client_id",
      "vault_id",
      "weight_g",
      "deposit_date"
    ],
    "rows": []
  }
}
```

---

## Задание 012: Удалить клиента

**Тип:** `delete`  
**Сложность:** 1/3  

📝 Файл для решения: [`student_solutions/012_delete_client.sql`](student_solutions/012_delete_client.sql)

### Пример данных для отображения:
```json
{
  "clients": {
    "columns": [
      "id",
      "full_name",
      "passport_number",
      "created_at"
    ],
    "rows": []
  },
  "vaults": {
    "columns": [
      "id",
      "vault_name",
      "capacity_g",
      "location"
    ],
    "rows": []
  },
  "gold_deposits": {
    "columns": [
      "id",
      "client_id",
      "vault_id",
      "weight_g",
      "deposit_date"
    ],
    "rows": [
      [
        248,
        1,
        704,
        684.57,
        "2025-07-19"
      ]
    ]
  }
}
```

---

## Задание 013: Выбрать имена клиентов и вес депозитов больше 500 грамм

**Тип:** `select`  
**Сложность:** 1/3  

📝 Файл для решения: [`student_solutions/013_select_large_deposits_join.sql`](student_solutions/013_select_large_deposits_join.sql)

### Пример данных для отображения:
```json
{
  "clients": {
    "columns": [
      "id",
      "full_name",
      "passport_number",
      "created_at"
    ],
    "rows": [
      [
        887,
        "Климент",
        "228998077660",
        null
      ]
    ]
  },
  "vaults": {
    "columns": [
      "id",
      "vault_name",
      "capacity_g",
      "location"
    ],
    "rows": []
  },
  "gold_deposits": {
    "columns": [
      "id",
      "client_id",
      "vault_id",
      "weight_g",
      "deposit_date"
    ],
    "rows": [
      [
        838,
        887,
        403,
        410.93,
        "2006-09-23"
      ]
    ]
  }
}
```


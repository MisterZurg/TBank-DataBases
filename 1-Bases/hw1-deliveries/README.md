# Практическое задание: работа с SELECT в системе доставки карт

## История
В банке работает система доставки банковских карт клиентам.  
Клиенты заказывают карты, а курьеры доставляют их по адресам.  
Петя, сотрудник банка, изучает SQL и учится извлекать полезные данные из базы.

В базе есть три таблицы:
- **clients** — клиенты, оформившие заказ,
- **couriers** — сотрудники-курьеры,
- **deliveries** — информация о доставках: кто, кому и когда доставил карту, а также стоимость доставки для банка.

Твоя задача — помочь Пете с запросами SELECT.  
Тебе предстоит выбирать, сортировать, объединять и фильтровать данные из этих таблиц.  
В некоторых заданиях нужно выйти за рамки изученного материала и использовать дополнительные функции.


Структура базы данных:

## Скрипт создания таблиц

```sql
CREATE TABLE clients (
    id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

CREATE TABLE couriers (
    id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

CREATE TABLE deliveries (
    id INT PRIMARY KEY,
    client_id INT,
    courier_id INT,
    delivery_date DATE,
    delivery_cost NUMERIC
);
```

---

## Примеры вставок данных 

```sql
-- Клиенты
INSERT INTO clients (id, first_name, last_name) VALUES
(1, 'Иван', 'Иванов'),
(2, 'Мария', 'Петрова');

-- Курьеры
INSERT INTO couriers (id, first_name, last_name) VALUES
(1, 'Сергей', 'Кузнецов'),
(2, 'Елена', 'Новикова');

-- Доставки
INSERT INTO deliveries (id, client_id, courier_id, delivery_date, delivery_cost) VALUES
(1, 1, 2, '2025-09-10', 500.00),
(2, 2, 1, '2025-09-11', 650.00);
```

---


### ⚙️ Инициализация базы данных
```sql
CREATE TABLE clients (id INT PRIMARY KEY, first_name VARCHAR(50), last_name VARCHAR(50)); CREATE TABLE couriers (id INT PRIMARY KEY, first_name VARCHAR(50), last_name VARCHAR(50)); CREATE TABLE deliveries (id INT PRIMARY KEY, client_id INT , courier_id INT, delivery_date DATE, delivery_cost NUMERIC);
```

### 🧹 Очистка между кейсами
```sql
DELETE FROM deliveries; DELETE FROM clients; DELETE FROM couriers;
```

### 💣 Полный сброс базы данных
```sql
DROP SCHEMA IF EXISTS public CASCADE; CREATE SCHEMA public;
```

---
### Задание 001: Вывести имена и фамилии всех клиентов
Файл для решения: [student_solutions/001_all_clients.sql](student_solutions/001_all_clients.sql)

---
### Задание 002: Вывести уникальные фамилии клиентов
Файл для решения: [student_solutions/002_unique_last_names.sql](student_solutions/002_unique_last_names.sql)

---
### Задание 003: Вывести всех курьеров, отсортировав по фамилии
Файл для решения: [student_solutions/003_couriers_sorted.sql](student_solutions/003_couriers_sorted.sql)

---
### Задание 004: Вывести первые три клиента по порядку id
Файл для решения: [student_solutions/004_limit_clients.sql](student_solutions/004_limit_clients.sql)

---
### Задание 005: Вывести полное имя клиента в формате 'Фамилия Имя' в поле full_name 
Файл для решения: [student_solutions/005_full_name_concat.sql](student_solutions/005_full_name_concat.sql)

---
### Задание 006: Вывести имена клиентов и стоимость их доставок с наценкой 10% (поле new_cost)
Файл для решения: [student_solutions/006_delivery_cost_bonus.sql](student_solutions/006_delivery_cost_bonus.sql)

---
### Задание 007: Вывести самую дорогую доставку
Файл для решения: [student_solutions/007_max_cost_delivery.sql](student_solutions/007_max_cost_delivery.sql)

---
### Задание 008: Вывести количество всех доставок
Файл для решения: [student_solutions/008_count_deliveries.sql](student_solutions/008_count_deliveries.sql)

---
### Задание 009: Вывести все поля клиентов и курьеров
Файл для решения: [student_solutions/009_all_fields_clients_couriers.sql](student_solutions/009_all_fields_clients_couriers.sql)

---
### Задание 010: Вывести имена клиентов и фамилии курьеров с явным указанием таблицы в запросе
Файл для решения: [student_solutions/010_select_fields_explicit_table.sql](student_solutions/010_select_fields_explicit_table.sql)

---
### Задание 011: Вывести имена клиентов как client_name
Файл для решения: [student_solutions/011_alias_first_name.sql](student_solutions/011_alias_first_name.sql)

---
### Задание 012: Вывести уникальные фамилии курьеров
Файл для решения: [student_solutions/012_distinct_courier_last.sql](student_solutions/012_distinct_courier_last.sql)

---
### Задание 013: Вывести полное имя клиента и фамилию курьера в одной строке в формате 'Фамилия Имя / Фамилия'
Файл для решения: [student_solutions/013_concat_client_courier.sql](student_solutions/013_concat_client_courier.sql)

---
### Задание 014: Вывести имена клиентов и удвоенную стоимость их доставок
Файл для решения: [student_solutions/014_double_delivery_cost.sql](student_solutions/014_double_delivery_cost.sql)

---
### Задание 015: Вывести имена клиентов, стоимость доставки с 10% наценкой и фамилию курьера
Файл для решения: [student_solutions/015_delivery_cost_bonus_courier.sql](student_solutions/015_delivery_cost_bonus_courier.sql)

---
### Задание 016: Вывести имена клиентов и стоимость доставок, умноженную на 12 и с конкатенацией фамилии курьера
Файл для решения: [student_solutions/016_yearly_cost_courier_concat.sql](student_solutions/016_yearly_cost_courier_concat.sql)

---
### Задание 017: Вывести первые две доставки с сортировкой по стоимости по убыванию
Файл для решения: [student_solutions/017_top_two_deliveries.sql](student_solutions/017_top_two_deliveries.sql)


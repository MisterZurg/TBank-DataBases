# Тест 1 Введение: зачем нужны базы данных

1. Что решают базы данных по сравнению с файлами (Excel, CSV, txt)? Хранят больше данных Исключают дублирование и ошибки обновления Делают работу с данными быстрее и надёжнее

- Все вышеперечисленное

2. Чем отличается база данных от СУБД?

- БД — это данные, СУБД — программа для управления ими


3. Какая модель данных используется в PostgreSQL?
- Реляционная



4. Какие преимущества есть у реляционной модели данных?

- Удобство работы с данными через SQL
- Возможность связей между таблицами
- Стандартизированная структура данных


5. Какой запрос выберет все данные из таблицы clients?

```sql
SELECT * FROM clients;
```


6. Как выбрать только фамилии клиентов?

```sql
SELECT last_name FROM clients;
```

7. Что делает оператор DISTINCT?

- Возвращает только уникальные значения в выборке


8. Что вернёт запрос:
```sql
SELECT DISTINCT courier_id FROM deliveries;
```

- Только уникальных курьеров, участвовавших в доставках

9. Какое слово используется для задания псевдонима столбца?

```sql
AS
```

10. Что покажет запрос:

```sql
SELECT delivery_cost, delivery_cost * 1.2 AS cost_with_vat FROM deliveries;
```

- Стоимость доставки и её увеличенный вариант на 20%


11. Что делает выражение `||` в SQL (PostgreSQL)?

- Конкатенация (склеивание строк)


12. Что делает запрос:
```sql
SELECT first_name || ' ' || last_name AS full_name FROM clients;
```

- Склеивает имя и фамилию клиента с пробелом между ними



13. Как отсортировать данные по убыванию стоимости доставки?

```sql
ORDER BY delivery_cost DESC;
```

14. Сопоставьте запрос и его результат

- Все доставки
- Доставки от самых старых к новым

```sql
-- 3 самые дорогие доставки
SELECT * FROM deliveries ORDER BY delivery_cost DESC LIMIT 3;
```

```sql
-- Уникальные курьеры
SELECT DISTINCT courier_id FROM deliveries;
```

```sql
-- Доставки от новых к старым
SELECT * FROM deliveries ORDER BY delivery_date DESC;
```

```sql
-- Фамилии клиентов с другим названием поля
SELECT last_name AS client_lastname FROM clients;
```


15. Что делает следующий запрос?

> [!CAUTION]
>
> Задача повышенной сложности, по не пройденному материалу

```sql
SELECT 
  d.delivery_date,
  c.first_name || ' ' || c.last_name AS client_full_name,
  cr.first_name || ' ' || cr.last_name AS courier_full_name,
  d.delivery_cost
FROM deliveries d
JOIN clients c ON d.client_id = c.id
JOIN couriers cr ON d.courier_id = cr.id;
```

- Объединяет данные из трёх таблиц
- Показывает дату, клиента, курьера и стоимость доставки

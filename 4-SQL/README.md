# Тест 4 SQL: SELECT, агрегаты, GROUP BY

## 1. Какой порядок выполнения операторов SQL в SELECT-запросе?

```sql
FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
```

## 2. Что делает оператор HAVING?
- Фильтрует группы после применения агрегатных функций

## 3. Какая из функций является агрегатной?
- COUNT
- SUM
- AVG

## 4. Сопоставьте SQL-операторы с их основной ролью
FROM Определяет таблицы для выборки
WHERE Фильтрует строки
GROUP BY Создаёт группы для агрегатных функций
HAVING Фильтрует группы
SELECT Выбирает столбцы и агрегаты
ORDER BY Сортирует результат
LIMIT  Ограничивает количество возвращаемых строк

## 5. Выберите правильный вариант подсчёта клиентов, сделавших больше 5 заказов.
```sql
SELECT client_id FROM orders GROUP BY client_id HAVING COUNT(*) > 5;
```

## 6. Что делает функция AVG?
- Вычисляет среднее значение по набору числовых данных


## 7. Выберите корректный запрос для подсчёта уникальных продуктов в заказах
```sql
SELECT COUNT(DISTINCT product_id) FROM orders;
```

## 8. Как ограничить результат выборки первыми 10 строками и отсортировать их по цене?
```sql
SELECT * FROM products ORDER BY price DESC LIMIT 10;
```

## 9. Выберите все верные варианты подзапросов для получения клиентов, сумма заказов которых выше средней.
```sql
SELECT * FROM clients WHERE id IN (SELECT client_id FROM orders GROUP BY client_id HAVING SUM(amount) > (SELECT AVG(total) FROM (SELECT SUM(amount) AS total FROM orders GROUP BY client_id) AS sub));
```

## 10. Выберите правильный запрос для получения средней цены по каждой категории для товаров с ценой > 100
```sql
SELECT category, AVG(price) FROM products WHERE price > 100 GROUP BY category;
```

## 11. Что будет выполняться первым в SQL-запросе: WHERE или HAVING?
- WHERE

## 12. Выберите правильный способ получить топ-5 самых дорогих товаров каждой категории
```sql
SELECT * FROM products p WHERE (SELECT COUNT(*) FROM products p2 WHERE p2.category = p.category AND p2.price > p.price) < 5;
```

## 13. Что делает оператор DISTINCT?
- Удаляет дубликаты из выборки

## 14. Выберите правильные варианты подсчёта клиентов, у которых сумма заказов по каждому товару > 100.
```sql
SELECT client_id FROM orders GROUP BY client_id, product_id HAVING SUM(amount) > 100;
```

## 15. Выберите корректные запросы для подсчёта клиентов с заказами только уникальных продуктов.
```sql
SELECT client_id FROM orders GROUP BY client_id HAVING COUNT(DISTINCT product_id) = COUNT(product_id);
```

## 16. Что делает ORDER BY в сочетании с LIMIT?
- Сортирует строки и ограничивает результат указанным количеством

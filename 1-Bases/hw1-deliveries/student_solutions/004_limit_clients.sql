-- Задание: Вывести первые три клиента по порядку id
SELECT
    first_name,
    last_name
FROM
    clients
ORDER BY id
LIMIT 3;
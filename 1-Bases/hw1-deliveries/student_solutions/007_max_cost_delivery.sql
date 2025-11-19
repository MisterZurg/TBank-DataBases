-- Задание: Вывести самую дорогую доставку
SELECT *
FROM
    deliveries
ORDER BY delivery_cost DESC
LIMIT 1
;
-- Задание: Вывести первые две доставки с сортировкой по стоимости по убыванию
SELECT
    *
FROM
    deliveries
ORDER BY delivery_cost DESC
LIMIT 2
;
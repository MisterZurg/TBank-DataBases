-- Задание: Вывести имена клиентов и стоимость их доставок с наценкой 10% (поле new_cost)
SELECT
    first_name,
    d.delivery_cost * 1.1 AS new_cost
FROM
    clients
LEFT JOIN
     deliveries AS d ON clients.id = d.client_id
;
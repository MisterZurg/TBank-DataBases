-- Задание: Вывести имена клиентов и удвоенную стоимость их доставок
SELECT
    cl.first_name,
    sum(delivery_cost) * 2
FROM clients AS cl
LEFT JOIN deliveries ON client_id = cl.id
GROUP BY
    cl.first_name
;
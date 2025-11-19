-- Задание: Вывести имена клиентов, стоимость доставки с 10% наценкой и фамилию курьера
SELECT
    cl.first_name,
    delivery_cost * 1.1,
    cr.last_name
FROM clients AS cl
LEFT JOIN deliveries ON client_id = cl.id
LEFT JOIN couriers AS cr ON cr.id = cl.id
;
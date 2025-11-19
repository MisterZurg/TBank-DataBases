-- Задание: Вывести имена клиентов и стоимость доставок, умноженную на 12 и с конкатенацией фамилии курьера
SELECT
    cl.first_name  || ' - '||  cr.last_name,
    sum(delivery_cost) * 12.0
FROM clients AS cl
         LEFT JOIN deliveries ON client_id = cl.id
         CROSS JOIN couriers AS cr -- ON cr.id = cl.id
group by
    cl.first_name, cr.last_name
;
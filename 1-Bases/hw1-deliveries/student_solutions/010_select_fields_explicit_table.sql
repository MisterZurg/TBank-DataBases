-- Задание: Вывести имена клиентов и фамилии курьеров с явным указанием таблицы в запросе
SELECT
    cl.first_name,
    cr.last_name
FROM clients AS cl
CROSS JOIN couriers AS cr
;
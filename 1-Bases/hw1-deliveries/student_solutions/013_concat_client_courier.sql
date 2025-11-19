-- Задание: Вывести полное имя клиента и фамилию курьера в одной строке в формате 'Фамилия Имя / Фамилия'
SELECT
    cl.first_name || ' ' || cl.last_name || ' / ' || cr.last_name
FROM
    clients AS cl
CROSS JOIN
    couriers AS cr
;
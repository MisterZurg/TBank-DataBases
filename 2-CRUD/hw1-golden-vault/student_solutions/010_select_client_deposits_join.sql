-- Задание 010: Выбрать имя клиента и вес его депозитов

-- Напишите ваше решение ниже:
SELECT
    cl.full_name,
    gd.weight_g
FROM
    clients AS cl
LEFT JOIN
    gold_deposits AS gd ON cl.id = gd.client_id
;
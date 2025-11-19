-- Задание 013: Выбрать имена клиентов и вес депозитов больше 500 грамм

-- Напишите ваше решение ниже:
SELECT
    cl.full_name,
    gd.weight_g
FROM
    clients AS cl
LEFT JOIN
    gold_deposits AS gd ON gd.client_id = cl.id
WHERE
    weight_g > 500
;
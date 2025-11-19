-- Задание 009: Посчитать общий вес золота в каждом хранилище

-- Напишите ваше решение ниже:
SELECT
    vault_id,
    sum(weight_g) as total_weight
FROM
    gold_deposits AS gd
LEFT JOIN
    vaults AS v ON v.id = gd.vault_id
GROUP BY
    vault_id
;


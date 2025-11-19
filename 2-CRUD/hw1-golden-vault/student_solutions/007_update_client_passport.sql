-- Задание 007: Обновить номер паспорта клиента

-- Напишите ваше решение ниже:
UPDATE clients
SET
    passport_number = '4500 654321'
WHERE
    id = 1
;
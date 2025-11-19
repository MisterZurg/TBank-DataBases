1 задание
1 балл
Что означает аббревиатура CRUD?


- Create, Read, Update, Delete


2 задание
1 балл
Какой SQL-оператор используется для добавления новых строк в таблицу?


UPDATE


ALTER TABLE


- INSERT INTO

ADD

3 задание
1 балл
Какой тип данных лучше использовать для хранения роста?




INT




4 задание
1 балл
Какие типы данных относятся к строковым?


VARCHAR


TEXT


CHAR




5 задание
1 балл
Что делает оператор DELETE FROM students WHERE id = 3;?


Удаляет всю таблицу students


- Удаляет только запись с id = 3


Удаляет столбец id


Ничего не делает


6 задание
1 балл
Какой оператор используется для изменения существующих данных?


ALTER


UPDATE


7 задание
1 балл
Какой запрос выберет всех студентов старше 18 лет?


SELECT * FROM students WHERE age = 18;


SELECT students WHERE age >= 18;


SELECT * FROM students WHERE age > 18;


8 задание
1 балл
Какой запрос корректно добавляет студента Алина Смирнова (19 лет, alina@mail.ru)


INSERT students VALUES ('Алина','Смирнова',19,'alina@mail.ru')


INSERT INTO students VALUES ('Алина','Смирнова',19,'alina@mail.ru');


9 задание
1 балл
Как обновить email студента с id = 2 на new@mail.com?




UPDATE students SET email = 'new@mail.com' WHERE id = 2;

10 задание
1 балл
Что делает оператор BETWEEN 10 AND 20?


Проверяет, входит ли значение в диапазон от 10 до 20


11 задание
2 балла
Соотнесите тип данных и пример значения:

Решение
'two'
'26-september-of-2025'
INT
42
VARCHAR
'Привет'
BOOLEAN
true
DATE
'2025-10-26'
Задание засчитывается, если все варианты будут правильно сопоставлены


12 задание
1 балл
Какой тип данных позволяет хранить вложенные объекты (полуструктурированные данные)?


JSONB

13 задание
1 балл
Как удалить всех студентов младше 18 лет?




DELETE FROM students WHERE age < 18;



14 задание
1 балл
Какой порядок выполнения логических операторов верный?


NOT > AND > OR


15 задание
1 балл
Какие выражения вернут true для строки 'Ivan' LIKE ...?


- 'Ivan' LIKE 'I%'


- 'Ivan' LIKE '%n'


'Ivan' LIKE '%v%'


- 'Ivan' LIKE 'Iv_n'


16 задание
1 балл
Какой результат вернёт выражение age BETWEEN 18 AND 25 при age = 17?


TRUE


FALSE


17 задание
1 балл
Какой запрос корректно создаёт таблицу courses?




CREATE TABLE courses (id SERIAL PRIMARY KEY, name VARCHAR(100), hours INT);



18 задание
1 балл
Вы ответили на все задания
Чтобы отправить их на проверку, нажмите «Завершить»
Какой запрос вернёт только фамилии всех студентов?


SELECT * FROM students;


SELECT last_name FROM students;

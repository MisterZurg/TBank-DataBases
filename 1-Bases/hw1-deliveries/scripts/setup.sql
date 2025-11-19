CREATE TABLE clients (id INT PRIMARY KEY, first_name VARCHAR(50), last_name VARCHAR(50));

CREATE TABLE couriers (id INT PRIMARY KEY, first_name VARCHAR(50), last_name VARCHAR(50));

CREATE TABLE deliveries (id INT PRIMARY KEY, client_id INT , courier_id INT, delivery_date DATE, delivery_cost NUMERIC);
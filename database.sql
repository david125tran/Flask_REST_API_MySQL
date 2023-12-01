DROP DATABASE IF EXISTS competitors_database;
CREATE DATABASE competitors_database;
USE competitors_database;
CREATE TABLE competitors_table(id INT,	name VARCHAR(50));

INSERT INTO competitors_table(id, name) VALUES (1, 'David'), (2, 'Jackie'), (3, 'Carmen');

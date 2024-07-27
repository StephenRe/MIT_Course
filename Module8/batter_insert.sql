DROP DATABASE IF EXISTS module_8_project;
CREATE DATABASE IF NOT EXISTS module_8_project;
USE module_8_project;
DROP TABLE IF EXISTS batting_average;
CREATE TABLE IF NOT EXISTS batting_average (Rk int, Pos varchar(5), Name varchar(50), BA float);
INSERT INTO batting_average(Rk,Pos,Name,BA)
VALUES
('1','C','Cal Raleigh#','0.219'),
('2','1B','Ty France','0.229'),
('3','2B','Jorge Polanco#','0.196'),
('4','SS','J.P. Crawford*','0.209'),
('5','3B','Josh Rojas*','0.245'),
('6','LF','Luke Raley*','0.241');
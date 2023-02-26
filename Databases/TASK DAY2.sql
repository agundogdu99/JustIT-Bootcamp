-- create 2 tables, at least 4 columns each. use all constraints like enum primary key foreign key, not null, default, auto increment
-- check.

CREATE DATABASE day2task;

USE day2task;

CREATE TABLE tutors (id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(15),
last_name VARCHAR(15), gender ENUM('Male', 'Female'), age INT NOT NULL CHECK (age>18), 
subject_taught VARCHAR(20) DEFAULT 'Bootcamp');

CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(15),
last_name VARCHAR(15), gender ENUM('Male', 'Female'), age INT NOT NULL, tutor_id INT, 
CHECK(age>18), FOREIGN KEY (tutor_id) REFERENCES tutors(id));

DESCRIBE tutors;
DESCRIBE students;

SELECT * FROM tutors;

-- 2nd TASK OF DAY 2

CREATE DATABASE day2task2;

CREATE TABLE student (passportNumber INT PRIMARY KEY AUTO_INCREMENT, studentFName VARCHAR(10) NOT NULL, studentLName VARCHAR(10),
studentAge INT DEFAULT '18' CHECK (studentAge>18))AUTO_INCREMENT = 10001;

CREATE TABLE course (courseID INT PRIMARY KEY, courseName ENUM('HTML', 'CSS', 'Javascript', 'Database', 'Python'), 
studentPassport INT, FOREIGN KEY (studentPassport) REFERENCES student(passportNumber));

USE TABLE student;
DROP TABLE student;
describe student;

INSERT INTO student (studentFName, studentLName, studentAge) VALUES ('Ahmet', 'Gundogdu', 35), ('Michael', 'Jordan', 55), ('Thierry', 'Henry', 42),
('Alan', 'Smith', 55), ('Harry', 'Kane', 30), ('Mikel', 'Arteta', 43), ('Alan', 'Sugar', 85), ('Thomas', 'Partey', 28);

INSERT INTO course (courseID, courseName, studentPassport) VALUES (1 , 'HTML', 10001), (2 , 'CSS', 10002), (3 , 'Javascript', 10003),
(4 , 'Database', 10004), (5 , 'Python', 10005), (6 , 'HTML', 10006), (7 , 'CSS', 10007), (8 , 'Javascript', 10008);


SELECT * FROM course JOIN student ON course.studentPassport = student.passportNumber;
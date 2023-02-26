-- SET SQL_SAFE_UPDATES = 0; -- Removes MYSQL safe mode!

-- CREATE DATABASE test2;
USE test2;
-- CREATE TABLE learners (learner_passport varchar(10) PRIMARY KEY,
-- first_name varchar(15) NOT NULL DEFAULT 'Unknown', last_name varchar(15),
-- dob DATE DEFAULT '2023-02-07');
-- describe learners;

-- CREATE TABLE courses (course_id INT auto_increment, course_subject varchar(10) NOT NULL DEFAULT 'Database',
-- learner_passport_number VARCHAR(10), PRIMARY KEY (course_id),
--  FOREIGN KEY (learner_passport_number) REFERENCES learners(learner_passport));
-- DESCRIBE courses;

-- CREATE TABLE tutor (ID INT PRIMARY KEY, age INT NOT NULL, gender ENUM('Male', 'Female'), CHECK(age>18));
-- DESCRIBE tutor;

-- INSERTING DATA INTO 'LEARNERS TABLE'
-- SYNTAX =  INSERT INTO <tableName> (Col1, Col2,...) VALUES (val1, val2...);
-- INSERT INTO learners (learner_passport, first_name, last_name, dob) VALUES ('0909874', 'Frank', 'Borg', '1980-02-07');
-- Insert multiple values
-- INSERT INTO learners (learner_passport, first_name, last_name, dob) VALUES ('073274', 'Mike', 'Smith', '1970-08-15'),
-- ('02124', 'Jim', NULL, '1970-08-15');
-- INSERT INTO learners (learner_passport, first_name) VALUES ('69678', 'Abdul');
SELECT * FROM learners;

INSERT INTO courses (course_subject, learner_passport_number) VALUES ('Databases', '073274');

INSERT INTO tutor (id, age, gender) VALUES (2, 20, 'FeMale');

SELECT * FROM learners;

-- Updating Records:
	-- One Column
		-- Syntax = UPDATE <tableName> SET <columnName> = <value> WHERE <condition>
	-- Multiple Columns
		-- Syntax = UPDATE <tableName> SET <columnName1> = <value>, <columnName2> = <value>...  WHERE <condition>

UPDATE learners SET first_name='Christian' WHERE learner_passport = '69678';

UPDATE learners SET first_name='Johnny', last_name='Bravo', learner_passport='0101010' WHERE learner_passport = '69678';

UPDATE learners SET first_name='Ahmet', last_name='Gundogdu', learner_passport='999999' 
WHERE learner_passport = '02124' AND first_name = 'Jim';
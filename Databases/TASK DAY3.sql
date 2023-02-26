-- DROP Foreign Key
ALTER TABLE course DROP FOREIGN KEY course_ibfk_1;

-- REMOVE PRIMARY KEY BACK FROM THE TABLE
	-- remove auto increment
ALTER TABLE students
MODIFY COLUMN passportNumber INT;

ALTER TABLE students DROP PRIMARY KEY;

-- ADD PRIMARY KEY BACK
ALTER TABLE students ADD PRIMARY KEY (passportNumber);

ALTER TABLE course ADD FOREIGN KEY(studentPassport) REFERENCES students(passportNumber);
show warnings;
describe course;

-- Day 3 2nd tasks
	-- From yesterdays tables
		-- remove and re-add back primary key
        -- remove foreign key and re-add foreign key
        -- delete some specific data
use day2task2;        
describe student;
describe course;

ALTER TABLE course MODIFY COLUMN courseID INT;
ALTER TABLE course DROP PRIMARY KEY;

ALTER TABLE course ADD PRIMARY KEY (courseID);
ALTER TABLE course MODIFY COLUMN courseID INT AUTO_INCREMENT;

ALTER TABLE course DROP FOREIGN KEY course_ibfk_1;
ALTER TABLE course ADD FOREIGN KEY(studentPassport) REFERENCES student(passportNumber);

ALTER TABLE course ADD country VARCHAR(15);
SELECT * FROM course;
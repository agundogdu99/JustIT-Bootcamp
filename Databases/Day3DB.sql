USE test2;

-- ALTERING A TABLE
	-- SYNTAX = ALTER TABLE <tableName> ADD <columnName> <datatype>
ALTER TABLE student ADD Country VARCHAR(15);

	-- Adding a column in a specific location
		-- SYNTAX = ALTER TABLE <tableName> ADD <columnName> <datatype> AFTER/BEFORE <existingColumnName>
ALTER TABLE student ADD Salary INT AFTER passportNumber;

-- DROPPING a column from a table
	-- SYNTAX = ALTER TABLE <tableName> DROP COLUMN <columnName>;
ALTER TABLE student DROP COLUMN salary;

-- Changing DATA TYPE of a column
	-- ALTER TABLE <tableName> MODIFY COLUMN <columnName> <newDataType>;
ALTER TABLE student MODIFY COLUMN salary DECIMAL(5,5);
DESCRIBE students;

-- RENAMING a table
	-- ALTER TABLE <tabelName> RENAME TO <newTableName>
ALTER TABLE student RENAME TO students;

-- RENAMING a column
	-- ALTER TABLE <tableName> RENAME COLUMN <columnName> TO <NEWColumnName>
ALTER TABLE students RENAME COLUMN salary TO wages;

-- Add a PRIMARY KEY
	-- ALTER TABLE <tableName> ADD PRIMARY KEY (<columnName>)
    
-- DROP a PRIMARY KEY
	-- ALTER TABLE <tableName> DROP PRIMARY KEY
    
-- Adding a FOREIGN KEY
	-- ALTER TABLE <tableName> ADD FOREIGN KEY (<columnName) REFERENCES <secondTableName> (<columnName-PK>)

-- Drop a FOREIGN KEY
	-- ALTER TABLE <tableName> DROP FOREIGN KEY <constraintName>, DROP KEY <columnName>;
    
SELECT CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
FROM information_schema.KEY_COLUMN_USAGE
WHERE REFERENCED_TABLE_NAME IS NOT NULL;

-- SELECTING
	-- SELECT * FROM <table>;
    -- SELECT name, salary FROM <table>;
    -- SELECT name, salary FROM <table> LIMIT 5;
	-- SELECT * FROM <table> LIMIT 3 OFFSET 4;
USE day2task2;
SELECT * FROM student;
SELECT studentFName, studentAge FROM student;
SELECT * FROM student LIMIT 5;
SELECT * FROM student LIMIT 3 OFFSET 5;




-- ON DELETE CASCADE
	-- If there is a foreign key and you try to delete, it will delete the other rows in other tables that it is reference to.
    
    -- Nested Queries
		-- Using the result of one select statement to inform the result of another select statement
        -- Always aim to breakdown the query, then integrate them
        
-- ON DELETE SET NULL

========================================
-- Store Procedure - 
	-- Precompiled SQL Statement which will be stored in database. Like table, view, trigger...
    -- Using this reduces netwrok traffic
    -- Its good for security
    -- A downside is that it uses resources of the database
	-- Changing Delimiter - specifies the end of a MYSQL query i.e. ;
			-- syntax = DELIMITER $$
	-- Parameter - argument
		-- IN - Giving a value to the store procedure . getter
        -- OUT - Procedure giving value or data to the caller . setter
        -- IN OUT - Does the job of both in and out

-- DELIMITER $$
-- CREATE PROCEDURE storeProcedureName(parameters)
-- BEGIN
-- // body of store procedure
-- END$$

DELIMITER $$
CREATE PROCEDURE allEmployee()
BEGIN
SELECT * FROM employee;
END$$
CALL allEmployee();

DELIMITER $$
CREATE PROCEDURE selectEmployee(IN firstName VARCHAR(20))
BEGIN
SELECT * FROM employee WHERE Fname = firstName;
END$$
CALL selectEmployee('JAMES')

TASK
-- Create store procedure which selects a user record based on the first name and last name
DELIMITER $$
CREATE PROCEDURE selectFullEmployee(IN firstName VARCHAR(20), IN lastName VARCHAR(20))
BEGIN
SELECT * FROM employee WHERE Fname = firstName AND Lname = lastName;
END$$
CALL selectFullEmployee('JAMES', 'BORG')

-- Store Procedure that selects all departments
DELIMITER $$
CREATE PROCEDURE selectAllDept()
BEGIN
SELECT * FROM Department;
END$$
CALL selectAllDept()

-- Procedure which deletes a record based on the parameter value
DELIMITER $$
CREATE PROCEDURE deleteParam(IN p_table VARCHAR(50), IN p_param VARCHAR(50), IN p_value VARCHAR(50))
BEGIN
DELETE FROM p_table WHERE p_param = p_value;
END$$
CALL deleteParam(a, y, z);

-- Select maximum salary from employee table - OUT	
USE COMPANY2;
DELIMITER ***
CREATE PROCEDURE maxSalary(OUT maxSalary INT)
BEGIN
SELECT MAX(SALARY) INTO maxSalary FROM Employee;
END***

CALL maxSalary(@maxSalary);
SELECT @maxSalary;

DROP PROCEDURE maxSalary;

-- zaks
USE Company;
DELIMITER ***
CREATE PROCEDURE maxSalary(OUT maxSalary INT)
BEGIN
SELECT MAX(SALARY) INTO maxSalary FROM Employee;
END***
CALL maxSalary(@maxsal);
SELECT @maxsal; USE test1;
DROP PROCEDURE maxSalary; -- delete procedure


-- Average Salary BASED ON GENDER - IN OUT
DELIMITER %%
CREATE PROCEDURE AvgSalaryGender(IN gender ENUM('m', 'f'), OUT avgSalary INT)
BEGIN
SELECT AVG(SALARY) INTO avgSalary FROM Employee WHERE sex = gender;
END%%
CALL avgSalaryGender('f', @avgSalary);
SELECT @avgSalary;

-- 
DELIMITER %%
CREATE PROCEDURE createPetTable(IN _TableName VARCHAR(20), IN _PetName VARCHAR(20), IN _PetDOB DATE, IN _PetType VARCHAR(20))
BEGIN
CREATE TABLE IF NOT EXISTS _TableName (PetName VARCHAR(20), PetDOB DATE, PetType VARCHAR(20));
INSERT INTO _TableName VALUES (_PetName , _PetDOB, _PetType);
END%%
CALL createPetTable('PetTable', 'Rocky', '2018-05-05', 'Dog');

=======

SELECT * FROM _tablename;

DROP PROCEDURE createPetTable;
DROP table _tablename;
=====================================
	
    -- i.e. Find all employees in research department
    SELECT * FROM employee WHERE DNO =(
    SELECT Dnumber FROM department WHERE DNAME = 'Research');
    
    -- another example...
    SELECT DNAME FROM department WHERE DNUMBER IN(
    SELECT DNUMBER FROM dept_locations WHERE DLOCATION = 'Houston');
    
    -- TASK
    -- FIND ALL Employees in the department that James Borg manages
    SELECT * FROM Employee WHERE DNO = ( SELECT DNO FROM Employee WHERE Fname='James' AND Lname = 'Borg');
    
    -- Select current date
    SELECT CURDATE();
    -- Retrieve current user name
    SELECT CURRENT_USER();
    -- retrieve current time
     SELECT CURRENT_TIME();
    -- retrieve current date and time
     SELECT NOW();
    -- retrieve reverse of hello text
    SELECT REVERSE('HELLO');
    -- remove extra spaces for '             hello            ' text
     SELECT TRIM('          HELLO                ');
    
    

    
    
==============
	SELECT COUNT(DNUM) FROM Project;
	SELECT * FROM Project WHERE (SELECT COUNT(DNUM) FROM Project) > 1;

	SELECT DNAME FROM department WHERE dnumber IN(
	SELECT DNUM FROM PROJECT GROUP BY DNUM HAVING COUNT(*)>1);
=============

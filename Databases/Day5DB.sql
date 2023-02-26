USE Company2;
SELECT * FROM employee;

-- Write a query to select all employees who's salary is greater than 30000 and sort them by thier date of birth
SELECT * FROM employee WHERE salary > '30000' ORDER BY Bdate DESC;
-- Write a query to select all employee who don't have manager.
SELECT * FROM employee WHERE Superssn IS NULL;
==================================================================
-- FUNCTIONS

COUNT(), MIN(), MAX(), AVG(), SUM(), ROUND()

-- How many records are in employee table?
SELECT COUNT(*) FROM employee;
    
-- Minimum/Maximum salary of an employee
SELECT MIN(SALARY) FROM employee;
SELECT MAX(SALARY) FROM employee;
-- AVERAGE salary
SELECT AVG(SALARY) FROM employee;
-- Total of all salaries
SELECT SUM(SALARY) FROM employee;


-- TASK
	-- TOTAL OF ALL SALARIES
SELECT SUM(SALARY) FROM employee;
	-- Total salary for employees who are Male
SELECT SUM(SALARY) FROM employee WHERE sex = "M";
	-- Find minimum and maximum in one query. rename column
SELECT MIN(SALARY) AS 'Minimum Salary', MAX(SALARY) AS 'Maximum Salary' FROM employee;

==========================================================================
-- GROUP BY --

-- How many males and females are in employee table?
SELECT sex, COUNT(sex) FROM employee GROUP BY sex;
-- How many people or on  a particular salary
SELECT salary, COUNT(*) FROM employee GROUP BY Salary;

-- TASK 
-- Select TOTAL, MAX, MINIMUM AND AVERAGE of salaries for all different genders
SELECT sex, SUM(salary) AS 'Total', 
MAX(salary) AS 'Maximum Salary', 
MIN(salary) AS 'Minimum Salary', 
AVG(salary) AS 'Average Salary' 
FROM employee GROUP BY sex;

=============================================
-- CONCAT
-- Retrieve 2 different cells at once i.e full name
SELECT CONCAT(Fname, ' ', lname)AS 'Full Name', CONCAT('£', Salary) FROM employee;

====================================
-- LIKE - WILDCARD

-- % Any number of characters
-- _ ONE character

-- Find employee record who's name starts with A
	SELECT * FROM employee WHERE Fname LIKE 'A%';
    -- Ends with N
	SELECT * FROM employee WHERE Fname LIKE '%N';
		-- Above in one query
        	SELECT * FROM employee WHERE Fname LIKE 'A%N';
            
	-- All records that have at least 5 characters and ends with N
    	SELECT * FROM employee WHERE Fname LIKE '%____N';
        
	-- All records that have OY in their name
	SELECT * FROM employee WHERE Fname LIKE '%OY%';
    
    -- Has OY and 2 more letters afterwards
	SELECT * FROM employee WHERE Fname LIKE '%OY__';


-- TASK

-- Select all employees whos name starts with J
SELECT * FROM employee WHERE Fname LIKE 'J%';
-- last name has 'LI'
SELECT * FROM employee WHERE Lname LIKE '%li%';
-- has 'OH' after first character of first name
SELECT * FROM employee WHERE Fname LIKE '_oh%';
-- Has 'ramesh' in their first name
SELECT * FROM employee WHERE Fname LIKE '%ramesh%';
-- record of employee who is born in 1965
SELECT * FROM employee WHERE Bdate LIKE '%1965%';
-- name has at least 5 characters
SELECT * FROM employee WHERE Fname LIKE '_____';
-- Who has 'M' as 3rd charavter in their first name and first name is at least 5 characters
SELECT * FROM employee WHERE Fname LIKE '__m__';
-- Starts with A and not ending with n
SELECT * FROM employee WHERE Fname LIKE '%a' AND Fname NOT LIKE '%n';

-- selec the sum of salaries for those male and females seperately whos salary is 
-- greater than 25000 - using concat function to retrieve them in one column
SELECT CONCAT(sex, ' Salary is £', SUM(salary)) FROM employee WHERE salary >= '25000' GROUP BY sex;

===============================================================================
-- 
-- HAVING clause
	-- Used in the select statement to specify filter condition for a group of rows or aggregate functions
    -- It is often used with GROUP BY clause to filter the group based on specific condition
    -- If we omit the GROUP BY clause, the HAVING clause behaves like a WHERE clause
    -- The HAVING clause applies a filter to each group of rows, while the WHERE clause applies filter to each individual row
    -- SELECT columnList FROM tableName WHERE <searchCondition> GROUP BY <groupColumn> HAVING <groupCondition>
    
-- Retreive Count of employees where more than 3 of them are working in the same department.
SELECT COUNT(*) FROM employee GROUP BY dno HAVING COUNT(dno) > 3;
    
-- retreive count of employees, total amount of salaries for those employees where 3 or more of them are working in same department.
SELECT COUNT(*), SUM(salary) FROM employee GROUP BY dno HAVING COUNT(dno) >= 3;

SELECT dno, COUNT(dno) FROM employee WHERE dno = '5';
SELECT dno, COUNT(dno) FROM employee GROUP BY dno;
SELECT dno, CONCAT(COUNT(*), ' people receive more than $25,000') FROM employee WHERE salary > '25000' GROUP BY dno;


SELECT dno, COUNT(dno) FROM employee WHERE salary > '25000' GROUP BY dno HAVING COUNT(dno) > 2;



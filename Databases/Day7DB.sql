String Functions
CONCAT()
	-- Concatenate strings, columns
TRIM()
	-- Removes extra spaces
LTRIM()
	-- Removes extra space only from left of string/value
RTRIM()
	-- As Above from right
    
LOWER(), LCASE()
	-- Convert all text to lowercase
UPPER(), UCASE()
	-- Convert all text to Uppercase
REVERSE()
	-- Returns the reverse of a string
    
SUBSSTRING()
	-- Extract substring from a string
    
SELECT REPLACE('AHMET GUNDOGDU', 'GUNDOGDU', 'GUNGUN')
	-- Replace a specific text in a string
    
SELECT CURRENT_USER()
SELECT NOW();
SELECT CURRENT_TIMESTAMP();
SELECT CURRENT_DATE();
SELECT CURRENT_TIME();

-- INSERT IGNORE --
	-- Ignores the problematic INSERTs and still inserts correct formatted ones
DESCRIBE dept_locations;

INSERT IGNORE INTO dept_locations (Dnumber, Dlocation)
VALUES (100, 'London'), (85, 'London');

SELECT * FROM dept_locations;

------------- BETWEEN ----------
-- Select records within a given range. Value can be text, number and date.
-- The beginning and end values are INCLUSIVE

-- I.E. Select all employees who are receiving salary between 20-30k
SELECT * FROM employee
WHERE Salary BETWEEN 20000 AND 30000;

SELECT * FROM employee
WHERE Bdate BETWEEN '1969-01-01' AND NOW();

-- TASK
-- Retrieve all employee names in uppercase
SELECT UPPER(Fname) FROM employee;
-- Retrieve all employees first name and remove extra spaces
SELECT TRIM(Fname) FROM employee;
-- Retrieve all employees full names in lowercase
SELECT LOWER(Fname), LOWER(Lname) FROM employee;


-------------------------------------------------------------------------- 

-- Another way of joining without JOIN

SELECT country.name, city.name, CountryLanguage.language
FROM Country, City, CountryLanguage
WHERE Country.code = City.CountryCode AND CountryLanguage.CountryCode = Country.code;

-- TASK 
-- RETRIEVE ALL EMPLOYEES AND THEIR DEPARTMENT NAMES
USE COMPANY2;
SELECT CONCAT(Employee.Fname, ' ', Employee.Lname), Department.Dname FROM Employee, Department
WHERE Employee.dno = Department.Dnumber;

-- Retrieve projects name and the employees name who are working on the project

SELECT Works_on.pno, Project.Pname, CONCAT(Employee.Fname, ' ', Employee.Lname) FROM Works_on, Project, Employee
WHERE project.pnumber = Works_on.Pno AND works_on.essn = employee.ssn;


-- Retrieve all employees who are working on more than 2 projects
-- Solution 1
SELECT DISTINCT Works_on.pno, Works_on.essn, Project.Pname, CONCAT(Employee.Fname, ' ', Employee.Lname) AS 'Name'
FROM Works_on, Project, Employee
WHERE project.pnumber = Works_on.Pno AND works_on.essn = employee.ssn 
AND Works_on.essn IN (
  SELECT Works_on.essn
  FROM Works_on
  GROUP BY Works_on.essn
  HAVING COUNT(*) > 2
)
GROUP BY 1, 2, 3, 4
ORDER BY name;

-- Solution 2
SELECT Works_on.pno, Project.Pname, CONCAT(Employee.Fname, ' ', Employee.Lname) AS 'Name'
FROM Works_on
JOIN Project ON Project.pnumber = Works_on.pno
JOIN Employee ON Employee.ssn = Works_on.essn
WHERE Works_on.essn IN (
  SELECT Works_on.essn
  FROM Works_on
  GROUP BY Works_on.essn
  HAVING COUNT(*) > 2
)
ORDER BY Name;

SELECT essn, COUNT(*) FROM Works_on GROUP BY essn HAVING COUNT(*) > 2;

SELECT Works_on.essn, COUNT(*) AS 'NumProjects'
FROM Works_on
GROUP BY Works_on.essn
HAVING COUNT(*) > 2;

-- Select all departments that have more than 3 projects 
SELECT department.dname, department.dnumber, COUNT(project.dnum) AS 'Projects'
FROM department
JOIN project
ON department.dnumber = project.dnum
GROUP BY 1, 2
HAVING COUNT(Project.dnum) > 2; -- (Changed to 2 as no results otherwise)

-- Select those departments which have more than 2 employees
SELECT department.dname, department.dnumber, COUNT(employee.dno) AS 'Employees'
FROM department
JOIN Employee
ON department.dnumber = employee.dno
GROUP BY 1, 2
HAVING COUNT(employee.dno) > 2;

-- - retreive Employee Full Name and Number of Hours for an employee who is working more than 40 hours
SELECT * FROM project;
SELECT * FROM works_on;
SELECT * FROM department;
SELECT * FROM dept_locations;
SELECT * FROM employee;
SELECT * FROM dependant;

SELECT employee.Fname, employee.Lname, SUM(works_on.hours) AS 'Hours'
FROM Employee
JOIN Works_on
ON Employee.ssn = works_on.essn
GROUP BY 1, 2;

SELECT CONCAT(employee.Fname, ' ', employee.Lname) AS 'Full Name', SUM(works_on.hours) AS 'Hours'
FROM Employee
JOIN Works_on
ON Employee.ssn = works_on.essn
GROUP BY 1
HAVING SUM(Works_on.hours) >= 40;

=====================================================================================================

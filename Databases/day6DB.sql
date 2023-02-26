SELECT * FROM employee;
SELECT * FROM DEPARTMENT;
SELECT * FROM DEPT_LOCATIONS;

-- UNION
SELECT DNUMBER FROM DEPARTMENT
UNION
SELECT DNUMBER FROM DEPT_LOCATIONS;

-- UNION ALL
SELECT DNUMBER FROM DEPARTMENT
UNION ALL
SELECT DNUMBER FROM DEPT_LOCATIONS;


-- JOINS
	 -- INNER JOIN
SELECT * FROM employee
INNER JOIN department
ON employee.DNO = department.dnumber;

SELECT Fname, Lname, dno, department.dname FROM employee
INNER JOIN department
ON employee.dno = department.dnumber;

	-- LEFT JOIN - All data on left table stays
SELECT Fname, Lname, dno, department.dname FROM employee
LEFT JOIN department
ON employee.dno = department.dnumber;

	-- RIGHT JOIN
SELECT Fname, Lname, dno, department.dname FROM employee
RIGHT JOIN department
ON employee.dno = department.dnumber;

	-- SELF JOIN 
SELECT CONCAT(a.Fname, ' ', a.Lname, ' ', a.Ssn) AS Manager, CONCAT(b.Fname, ' ', b.Lname, ' ', b.Superssn) AS Employee
FROM employee a
JOIN employee b
ON a.Ssn = b.Superssn;


-- Tasks
	-- for next day
    
    -- Select all countries name and their city name and population
    -- select all countries name and their official languages
    -- select country name, city name which have more than 3 cities
    -- select those countries and their languages which have more than 2 official languages
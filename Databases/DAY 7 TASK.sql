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
SELECT CONCAT(employee.Fname, ' ', employee.Lname) AS 'Full Name', SUM(works_on.hours) AS 'Hours'
FROM Employee
JOIN Works_on
ON Employee.ssn = works_on.essn
GROUP BY 1
HAVING SUM(Works_on.hours) >= 40;
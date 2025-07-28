# Write your MySQL query statement below
SELECT 
    d.name AS Department, 
    e.name AS Employee, 
    e.salary AS Salary
FROM Employee e
JOIN Department d
JOIN (
    SELECT departmentId, MAX(salary) AS salary
    FROM Employee
    GROUP BY departmentId
) AS s
WHERE d.id = s.departmentId AND e.salary = s.salary
# Write your MySQL query statement below
WITH base AS (
    SELECT
        d.name AS Department,
        e.name AS Employee,
        e.salary AS Salary,
        DENSE_RANK() OVER (PARTITION BY d.id ORDER BY salary DESC) AS rankings
    FROM
        Employee AS e
    LEFT JOIN
        Department AS d
        ON e.departmentId = d.id    
)

SELECT
    Department,
    Employee,
    Salary
FROM
    base
WHERE
    rankings <= 3
-- Write your PostgreSQL query statement below
WITH salary_rank_table AS (
    SELECT
        d.name AS Department,
        e.name AS Employee,
        e.salary,
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS salary_rank
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
    salary_rank_table
WHERE 
    salary_rank = 1
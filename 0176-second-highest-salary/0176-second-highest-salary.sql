-- Write your PostgreSQL query statement below
WITH rank_table AS(
    SELECT
        *,
        DENSE_RANK() OVER(ORDER BY salary DESC) AS salary_rank
    FROM 
        Employee
)

SELECT
    MAX(salary) AS SecondHighestSalary
FROM
    rank_table
WHERE
    salary_rank = 2

-- SELECT
--     DISTINCT salary
-- FROM
--     Employee
-- ORDER BY 
--     salary DESC
-- LIMIT 
--     2
-- Write your PostgreSQL query statement below
WITH five_reports AS (
    SELECT
        e1.id
    FROM
        Employee AS e1
    LEFT JOIN 
        Employee AS e2
        ON e1.id = e2.managerid
    GROUP BY
        e1.id
    HAVING 
        COUNT(*) >= 5
)

SELECT
    name
FROM
    Employee
WHERE
    id IN (
        SELECT
            *
        FROM
            five_reports
    )
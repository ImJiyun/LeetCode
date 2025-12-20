# Write your MySQL query statement below
WITH daily_amount AS (
    SELECT
        visited_on,
        SUM(amount) AS amount
    FROM
        Customer
    GROUP BY
        visited_on
), rolling_7days AS (
    SELECT
        visited_on,
        ROW_NUMBER() OVER (ORDER BY visited_on) AS rn,
        SUM(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
        ROUND(
            AVG(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW),
            2
        ) AS average_amount
    FROM
        daily_amount
)

SELECT
    visited_on,
    amount,
    average_amount
FROM
    rolling_7days
WHERE 
    rn > 6
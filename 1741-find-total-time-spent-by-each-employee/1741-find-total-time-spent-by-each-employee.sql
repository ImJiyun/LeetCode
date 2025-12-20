# Write your MySQL query statement below
WITH time_diff AS (
    SELECT
        *,
        out_time - in_time AS diff
    FROM
        Employees
)

SELECT
    event_day AS day,
    emp_id, 
    SUM(diff) AS total_time
FROM
    time_diff
GROUP BY
    emp_id, 
    event_day
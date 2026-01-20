# Write your MySQL query statement below
WITH add_previous_date AS (
    SELECT
        *,
        DENSE_RANK() OVER (PARTITION BY player_id ORDER BY event_date) AS login_cnt,
        LAG(event_date, 1) OVER (PARTITION BY player_id ORDER BY event_date) AS previous_date
    FROM
        Activity 
)


SELECT
    ROUND(
        (COUNT(DISTINCT player_id))/
        (
            SELECT
                COUNT(DISTINCT player_id)
            FROM 
                Activity
        ),
        2 
    ) AS fraction 
FROM
    add_previous_date
WHERE
    login_cnt = 2 AND DATEDIFF(event_date, previous_date) = 1
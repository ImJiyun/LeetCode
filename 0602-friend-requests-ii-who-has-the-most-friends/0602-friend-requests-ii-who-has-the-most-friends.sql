# Write your MySQL query statement below
WITH union_table AS (
    SELECT
        *
    FROM
        RequestAccepted
    UNION ALL
    SELECT
        accepter_id,
        requester_id,
        accept_date 
    FROM
        RequestAccepted
), friend_cnts AS (
    SELECT
        requester_id AS id,
        COUNT(requester_id) AS num
    FROM
        union_table
    GROUP BY
        requester_id 
)

SELECT
    id,
    num
FROM (
    SELECT
        *,
        RANK() OVER (ORDER BY num DESC) AS rn
    FROM
        friend_cnts
) AS t
WHERE
    rn = 1
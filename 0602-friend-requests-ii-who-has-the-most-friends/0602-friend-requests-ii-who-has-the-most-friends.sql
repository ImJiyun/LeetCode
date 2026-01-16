# Write your MySQL query statement below
-- WITH union_table AS (
--     SELECT
--         *
--     FROM
--         RequestAccepted
--     UNION ALL
--     SELECT
--         accepter_id,
--         requester_id,
--         accept_date 
--     FROM
--         RequestAccepted
-- ), friend_cnts AS (
--     SELECT
--         requester_id AS id,
--         COUNT(requester_id) AS num
--     FROM
--         union_table
--     GROUP BY
--         requester_id 
-- )

-- SELECT
--     id,
--     num
-- FROM (
--     SELECT
--         *,
--         RANK() OVER (ORDER BY num DESC) AS rn
--     FROM
--         friend_cnts
-- ) AS t
-- WHERE
--     rn = 1


-- WITH BASE AS(
--     SELECT
--         requester_id,
--         COUNT(requester_id) as cnt_r
       
--     FROM RequestAccepted
--     GROUP BY
--         requester_id
        
-- )

-- WITH BASE_2 AS (
--     SELECT
--         accepter_id,
--         count(accepter_id) as cnt_a
--     from

-- SELECT
-- *
-- FROM BASE

SELECT 
    base.id,
    (
        (SELECT COUNT(*) FROM RequestAccepted WHERE requester_id = base.id) +
        (SELECT COUNT(*) FROM RequestAccepted WHERE accepter_id = base.id)
) AS num
FROM (
    SELECT requester_id AS id FROM RequestAccepted
    UNION
    SELECT accepter_id AS id FROM RequestAccepted
) AS base
ORDER BY num DESC
LIMIT 1;
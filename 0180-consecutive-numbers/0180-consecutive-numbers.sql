# Write your MySQL query statement below
# 처음 시도 : 10/23 testcase passed
-- WITH lag_lead_table AS (
--     SELECT
--         *,
--         LAG(num, 2) OVER (ORDER BY id) AS prev_num,
--         LEAD(num, 2) OVER (ORDER BY id) AS next_num
--     FROM 
--         Logs
-- )

-- SELECT
--     num AS ConsecutiveNums 
-- FROM
--     lag_lead_table
-- WHERE
--     num = prev_num 
--     AND
--     prev_num = next_num  

WITH lag_lead_table AS (
    SELECT
        *,
        LAG(num, 1) OVER (ORDER BY id) AS prev_num,
        LAG(num, 2) OVER (ORDER BY id) AS prev_prev_num
    FROM 
        Logs
)

# DISTINCT 안 썼더니 19 / 23 testcases passed

SELECT
    DISTINCT num AS ConsecutiveNums 
FROM
    lag_lead_table
WHERE
    num = prev_num 
    AND
    prev_num = prev_prev_num  
# Write your MySQL query statement below
# Every derived table must have its own alias
SELECT 
    MAX(num) as num
FROM (
    SELECT
        num,
        COUNT(num) as cnt
    FROM
        MyNumbers
    GROUP BY
        num
    HAVING
        cnt = 1
    ORDER BY
        num DESC 
    LIMIT 
        1
) as t
# Write your MySQL query statement below
SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT 
        num,
        LAG(num, 1) OVER (ORDER BY id) AS prev1,
        LAG(num, 2) OVER (ORDER BY id) AS prev2 
    FROM Logs
) AS t
WHERE num = prev1 AND num = prev2
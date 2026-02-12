# Write your MySQL query statement below
SELECT
    DISTINCT t1.id,
    -- t1.p_id,
    -- t2.id AS c_id,
    CASE 
        WHEN t1.p_id IS NULL THEN 'Root'
        WHEN t1.p_id IS NOT NULL AND t2.id IS NOT NULL THEN 'Inner'
        WHEN t1.p_id IS NOT NULL AND t2.id IS NULL THEN 'Leaf'
    END AS type
FROM
    Tree AS t1
LEFT JOIN
    Tree AS t2
ON 
    t1.id = t2.p_id
# Write your MySQL query statement below
WITH base AS (
    SELECT
        buyer_id,
        join_date,
        COUNT(user_id) AS orders_in_2019 
    FROM
        Users AS u 
    LEFT JOIN
        Orders AS o
    ON 
        u.user_id = o.buyer_id 
    WHERE
        DATE_FORMAT(order_date, '%Y') = '2019'
    GROUP BY
        buyer_id 
)

SELECT
    IF(buyer_id IS NULL, user_id, buyer_id) AS buyer_id,
    IF(b.join_date IS NULL, t.join_date, b.join_date) AS join_date,
    IF(orders_in_2019 IS NULL, 0, orders_in_2019) AS orders_in_2019  
FROM (
    SELECT
        *
    FROM
        Users
) AS t
LEFT JOIN
    base AS b
ON 
    t.user_id = b.buyer_id
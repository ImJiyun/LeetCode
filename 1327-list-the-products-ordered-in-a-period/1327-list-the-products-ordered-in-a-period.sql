# Write your MySQL query statement below
SELECT
    t.product_name,
    t.unit_sum AS unit
FROM (
    SELECT
        p.product_id,
        p.product_name,
        SUM(unit) as unit_sum
    FROM
        Products p
    JOIN 
        Orders o
    ON 
        p.product_id = o.product_id
    WHERE
        DATE_FORMAT(order_date, '%Y-%m') = '2020-02'
    GROUP BY
        p.product_id
    HAVING
        unit_sum >= 100
) AS t
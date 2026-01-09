-- Write your PostgreSQL query statement below
-- 첫 시도 
-- WITH rn_table AS (
--     SELECT
--         *,
--         ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY year) AS rn
--     FROM
--         Sales 
-- )

-- SELECT
--     product_id,
--     year AS first_year,
--     quantity,
--     price
-- FROM
--     rn_table
-- WHERE
--     rn = 1


-- 두 번째 시도


WITH rn_table AS (
    SELECT
        *,
        ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY year) AS rn
    FROM (
        SELECT
        product_id,
        year,
        SUM(quantity) AS quantity,
        price 
    FROM
        Sales
    GROUP BY
        product_id,
        year,
        price 
    ) 
)

SELECT
    product_id,
    year AS first_year,
    quantity,
    price
FROM
    rn_table
WHERE
    rn = 1

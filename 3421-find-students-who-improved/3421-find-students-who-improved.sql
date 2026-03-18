# Write your MySQL query statement below
-- WITH ranked AS (
--     SELECT
--         *,
--         ROW_NUMBER() OVER (PARTITION BY student_id, subject ORDER BY exam_date) AS rn_asc,
--         ROW_NUMBER() OVER (PARTITION BY student_id, subject ORDER BY exam_date DESC) AS rn_desc
--     FROM
--         Scores
-- )

-- SELECT 
--     student_id,
--     subject,
--     MAX(CASE WHEN rn_asc = 1 THEN score END) AS first_score,
--     MAX(CASE WHEN rn_desc = 1 THEN score END) AS latest_score
-- FROM
--     ranked
-- GROUP BY
--     student_id, 
--     subject
-- HAVING
--     first_score < latest_score

-- SELECT 
--     student_id,
--     subject,
--     CASE WHEN rn_asc = 1 THEN score END AS first_score,
--     CASE WHEN rn_desc = 1 THEN score END AS latest_score
-- FROM
--     ranked


WITH date_rn AS (
    SELECT
        *,
        RANK() OVER (PARTITION BY student_id, subject ORDER BY exam_date) AS first_date_rn,
        RANK() OVER (PARTITION BY student_id, subject ORDER BY exam_date DESC) AS last_date_rn
    FROM
        Scores
)

SELECT
    student_id,
    subject,
    MAX(CASE WHEN first_date_rn = 1 THEN score END) AS first_score,
    MAX(CASE WHEN last_date_rn = 1 THEN score END) AS latest_score
FROM
    date_rn
GROUP BY
    student_id, 
    subject
HAVING
    first_score < latest_score
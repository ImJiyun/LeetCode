CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
        SELECT
            DISTINCT salary 
        FROM
            (
                SELECT
                    salary,
                    DENSE_RANK() OVER (ORDER BY salary DESC) AS rankings
                FROM
                    Employee
            ) AS r
        WHERE
            rankings = N
  );
END
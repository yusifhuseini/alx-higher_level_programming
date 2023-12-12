-- Lists all records of table 'second_table' where name field is not empty
-- Records should be listed by descending score
-- The database name will be passed as an argument to the mysql command
SELECT
    score, name
FROM
    second_table
WHERE
    name IS NOT NULL
ORDER BY
    score DESC;

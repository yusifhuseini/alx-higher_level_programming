-- Updates the score of Bob to '10' in table 'second_table'
-- use 'name' field only to make this update
-- The database name will be passed as an argument of the mysql command
UPDATE
    second_table
SET
    score = 10
WHERE
    name = 'Bob';

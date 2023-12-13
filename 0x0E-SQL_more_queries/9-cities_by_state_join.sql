-- Lists all cities contained in the database hbtn_0d_usa
-- Each record should display: cities.id - cities.name - states.name
-- Results must be sorted in ascending order by cities.id
-- The database name will be passed as an argument of the mysql command
SELECT c.id, c.name, s.name
FROM cities AS c
LEFT JOIN states AS s
ON c.state_id = s.id
ORDER BY c.id ASC;

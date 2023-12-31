-- Creates database 'hbtn_0d_usa' and table 'states'
-- If the database hbtn_0d_usa already exists, your script should not fail
-- If the table states already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

/* Create table */
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256)
);

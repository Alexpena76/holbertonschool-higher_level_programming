-- Script that lists all cities of California in the database hbtn_0d_usa
-- Results are sorted by cities.id in ascending order

SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ASC;

-- Script that lists all records with a score >= 10
-- from the table second_table
-- Results display the score and the name (in this order)
-- Records are ordered by score (top first)

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;

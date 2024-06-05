-- SELECT (CASE WHEN count(num) = 1 THEN num ELSE null END) AS num
-- FROM mynumbers
-- GROUP BY num
-- ORDER BY count(num), num DESC
-- LIMIT 1;

SELECT max(num) AS num
FROM mynumbers
WHERE num IN (SELECT num FROM mynumbers GROUP BY num HAVING count(num) = 1);

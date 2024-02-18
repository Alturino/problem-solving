SELECT class
FROM courses
GROUP BY class
HAVING count(student) > 5;

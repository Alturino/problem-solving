SELECT
    teacher_id,
    count(DISTINCT subject_id) AS cnt
FROM teacher
WHERE teacher_id = teacher_id
GROUP BY teacher_id;

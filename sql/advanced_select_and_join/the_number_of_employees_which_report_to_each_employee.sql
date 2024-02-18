SELECT
    m.employee_id,
    m.name,
    count(m.employee_id) AS reports_count,
    round(avg(e.age)::numeric) AS average_age
FROM employees AS m
INNER JOIN employees AS e
    ON m.employee_id = e.reports_to
GROUP BY m.employee_id, m.name
ORDER BY m.employee_id;

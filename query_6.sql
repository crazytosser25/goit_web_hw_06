-- Знайти список студентів у певній групі.
SELECT
    students.student_id AS student_id,
    students.name AS student_name,
    groups.name AS group_name
FROM
    students
JOIN
    groups ON students.group_id = groups.group_id
WHERE
    groups.group_id = 17;

-- Знайти оцінки студентів у окремій групі з певного предмета.
SELECT
    students.name AS student_name,
    grades.grade AS grade,
    grades.date_received AS data_of_grade
FROM
    students
JOIN
    grades ON students.student_id = grades.student_id
JOIN
    subjects ON grades.subject_id = subjects.subject_id
JOIN
    groups ON students.group_id = groups.group_id
WHERE
    groups.group_id = 1
    AND grades.subject_id = 5;

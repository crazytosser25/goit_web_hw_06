-- Знайти середній бал у групах з певного предмета.
SELECT
    groups.group_id AS group_numer,
    groups.name AS group_name,
    subjects.name AS subject_name,
    AVG(grades.grade) AS avg_grade
FROM
    students
JOIN
    grades ON students.student_id = grades.student_id
JOIN
    groups ON students.group_id = groups.group_id
JOIN
    subjects ON grades.subject_id = subjects.subject_id
WHERE
    grades.subject_id = 2
GROUP BY
    groups.group_id
ORDER BY
    group_numer ASC;

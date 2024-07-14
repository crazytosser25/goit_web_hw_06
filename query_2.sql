-- Знайти студента із найвищим середнім балом з певного предмета.
SELECT
    students.name AS student_name,
    subjects.name AS subject_name,
    AVG(grades.grade) AS avg_grade
FROM
    students
JOIN
    grades ON students.student_id = grades.student_id
JOIN
    subjects ON grades.subject_id = subjects.subject_id
WHERE
    grades.subject_id = 9
GROUP BY
    students.student_id
ORDER BY
    avg_grade DESC
LIMIT 1;

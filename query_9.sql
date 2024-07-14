-- Знайти список курсів, які відвідує студент.
SELECT DISTINCT
    subjects.subject_id AS subject_id,
    subjects.name AS subject_name
FROM
    subjects
JOIN
    grades ON subjects.subject_id = grades.subject_id
WHERE
    grades.student_id = 123
ORDER BY
    subject_id ASC;

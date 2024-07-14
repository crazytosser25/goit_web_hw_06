-- Знайти середній бал, який ставить певний викладач зі своїх предметів.
SELECT
    professors.professor_id AS professor_id,
    professors.name AS professor_name,
    subjects.name AS subject_name,
    AVG(grades.grade) AS avg_grade
FROM
    professors
JOIN
    subjects ON professors.subject_id = subjects.subject_id
JOIN
    grades ON subjects.subject_id = grades.subject_id
WHERE
    professors.professor_id = 7

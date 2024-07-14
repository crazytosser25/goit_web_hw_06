-- Знайти які курси читає певний викладач.
SELECT
    subjects.subject_id,
    subjects.name AS subject_name,
    professors.name AS professor_name
FROM
    subjects
JOIN
    professors ON subjects.subject_id = professors.subject_id
WHERE
    professors.professor_id = 5;

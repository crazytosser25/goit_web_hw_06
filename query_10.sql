-- Список курсів, які певному студенту читає певний викладач.
SELECT DISTINCT
    subjects.subject_id,
    subjects.name AS subject_name
FROM
    subjects
JOIN
    grades ON subjects.subject_id = grades.subject_id
JOIN
    professors ON subjects.subject_id = professors.subject_id
WHERE
    grades.student_id = 128
    AND professors.professor_id = 5;

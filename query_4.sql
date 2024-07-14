-- Знайти середній бал на потоці (по всій таблиці оцінок).
SELECT
    AVG(grades.grade) AS avg_grade
FROM
    grades

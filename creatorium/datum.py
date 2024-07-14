"""Genetates test data into tables."""
import logging
import sqlite3
from random import randint, choice
from datetime import datetime, timedelta
from faker import Faker


def generate_data():
    try:
        conn = sqlite3.connect('base/college.db')
        cursor = conn.cursor()

        fake = Faker()

        group_ids = []
        for _ in range(randint(30, 40)):
            cursor.execute(
                'INSERT INTO groups (name) VALUES (?)',
                (fake.word().capitalize(),)
            )
            group_ids.append(cursor.lastrowid)

        subject_ids = []
        for _ in range(randint(10, 15)):
            cursor.execute(
                'INSERT INTO subjects (name) VALUES (?)',
                (fake.job().capitalize(),)
            )
            subject_ids.append(cursor.lastrowid)

        professor_ids = []
        for _ in range(randint(20, 25)):
            prof_name = f"Professor {fake.name()}"
            cursor.execute(
                'INSERT INTO professors (name, subject_id) VALUES (?, ?)',
                (prof_name, choice(subject_ids))
            )
            professor_ids.append(cursor.lastrowid)

        student_ids = []
        for _ in range(randint(350, 450)):
            cursor.execute(
                'INSERT INTO students (name, group_id) VALUES (?, ?)',
                (fake.name(), choice(group_ids))
            )
            student_ids.append(cursor.lastrowid)

        start_date = datetime.strptime('2024-01-01', '%Y-%m-%d')
        end_date = datetime.strptime('2024-06-30', '%Y-%m-%d')

        for student in student_ids:
            for _ in range(randint(15, 20)):
                subject = choice(subject_ids)
                grade = randint(50, 100)
                random_days = randint(0, (end_date - start_date).days)
                date_received = start_date + timedelta(days=random_days)
                date_formatted = date_received.strftime('%Y-%m-%d')
                professor = choice(professor_ids)
                cursor.execute('''
                    INSERT INTO grades (
                        student_id,
                        subject_id,
                        professor_id,
                        grade,
                        date_received
                    ) VALUES (?, ?, ?, ?, ?)''',
                    (student, subject, professor, grade, date_formatted)
                )

        conn.commit()

    except sqlite3.Error as e:
        logging.error(e)
    finally:
        conn.close()

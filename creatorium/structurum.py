"""Creating tabels structure"""
import logging
import sqlite3


def create_structure() -> None:
    try:
        conn = sqlite3.connect('base/college.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                group_id INTEGER,
                FOREIGN KEY (group_id) REFERENCES groups (group_id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS groups (
                group_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS subjects (
                subject_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS professors (
                professor_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                subject_id INTEGER NOT NULL,
                FOREIGN KEY (subject_id) REFERENCES subjects (subject_id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS grades (
                grade_id INTEGER PRIMARY KEY,
                student_id INTEGER,
                subject_id INTEGER,
                professor_id INTEGER,
                grade INTEGER NOT NULL,
                date_received DATE NOT NULL,
                FOREIGN KEY (student_id) REFERENCES students (student_id),
                FOREIGN KEY (subject_id) REFERENCES subjects (subject_id),
                FOREIGN KEY (professor_id) REFERENCES professors (professor_id)
            )
        ''')

        conn.commit()

    except sqlite3.Error as e:
        logging.error(e)
    finally:
        conn.close()

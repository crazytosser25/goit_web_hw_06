import sqlite3
import sys
import os
from pprint import pprint


def execute_query(sql: str) -> list:
    with sqlite3.connect('base/college.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

def main() -> None:
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("Usage: python3 base_reader.py sql_file")
        sys.exit(1)

    source_file = sys.argv[1]

    if not os.path.exists(source_file):
        print('No such directory.')
        sys.exit(1)
    with open(source_file, encoding = 'utf-8') as f:
        sql_query = f.read()

    pprint(execute_query(sql_query))


if __name__ == '__main__':
    main()

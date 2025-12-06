
# I have neither given nor received unauthorized assistance on this assignment.
# Generative AI statement: I used ChatGPT to help with SQL syntax, parameterized query formatting, and HTML table styling.


import sqlite3
import sys
from os.path import exists

if exists('cs_course_scheduling.sqlite'):
    conn = sqlite3.connect('cs_course_scheduling.sqlite')

    # ✅ check that a command-line argument was provided
    if len(sys.argv) < 2:
        print("Usage: python list_students.py <academic_year>")
        conn.close()
        exit()

    # ✅ get the academic year from command line (as integer)
    year = int(sys.argv[1])

    # ✅ parameterized query to prevent SQL injection
    cursor = conn.execute("""
        SELECT first_name, last_name, academic_year
        FROM students
        WHERE academic_year = ?
        ORDER BY last_name ASC
    """, (year,))

    for row in cursor:
        print("First Name = ", row[0])
        print("Last Name = ", row[1])
        print("Academic Year = ", row[2])
        print("----------------------------------------")

    conn.close()
    print("Database was accessed and closed")

else:
    print('Database file cs_course_scheduling.sqlite not found in current working directory.')

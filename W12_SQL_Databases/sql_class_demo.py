'''
Created 2023, updated 2025
@author: Siwei Cao, Patrick Sullivan
@attention: this is a template for you to practice sql
'''

from os.path import exists
import sqlite3
# see https://docs.python.org/3/library/sqlite3.html#sqlite3-tutorial

sqlFilePath = "REPLACE_ME_WITH_DATABASE_FILEPATH"

assert exists(sqlFilePath), f"File does not exist: {sqlFilePath}"

conn = sqlite3.connect(sqlFilePath)
cursor = conn.execute("REPLACE_ME_WITH_SQL_STATEMENTS")

# cursor is an object, iterate through it to manipulate output result
for item in cursor:
    # do something with item here
    pass # do-nothing placeholder for keeping python indented

conn.close()
print("Database was successfully accessed and closed")

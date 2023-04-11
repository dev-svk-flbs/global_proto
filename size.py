import os
import time




while True:

    database_path = 'db.sqlite3' # replace with your database file path
    database_size = os.path.getsize(database_path)

    print(f"Size of database file {database_path} is {database_size} bytes")
    time.sleep(2)

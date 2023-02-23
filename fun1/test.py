import sqlite3
import os
import pandas as pd


print(sqlite3.version)
print(sqlite3.sqlite_version)
path = os.path.dirname(__file__)
conn = sqlite3.connect(path + '\\table.db')
cur = conn.cursor()

save = pd.read_sql_query("select user_id from user", conn)

print(save)


conn.commit()
conn.close()

import sqlite3

dbfile = 'botuploads.db'

con = sqlite3.connect(dbfile)

cur = con.cursor()

table_list = [a for a in cur.execute("SELECT file_id FROM 'Media ids'")]
file_id_list = [0] * len(table_list)
for i in range(len(table_list)):
    file_id_list[i] = ''.join(table_list[i])

con.close()

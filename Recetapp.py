import sqlite3

conn = sqlite3.connect("penuche.db")

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS recetapp")

cursor.execute("CREATE TABLE IF NOT EXISTS recetapp(id integer PRIMARY KEY NOT NULL, nombre text)")

conn.commit()

conn.close()
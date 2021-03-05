import sqlite3

conn = sqlite3.connect("Recetapp.db")

cursor = conn.cursor()

conn.close()


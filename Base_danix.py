import sqlite3

conn = sqlite3.connect("lutsk_temperature.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS temperature (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    temperature REAL NOT NULL
)
''')

cursor.execute("INSERT INTO temperature (date, time, temperature) VALUES (?, ?, ?)", ("2025-01-15", "08:00", -2.5))
cursor.execute("INSERT INTO temperature (date, time, temperature) VALUES (?, ?, ?)", ("2025-01-16", "12:00", 0.0))
cursor.execute("INSERT INTO temperature (date, time, temperature) VALUES (?, ?, ?)", ("2025-01-17", "15:00", 1.2))
cursor.execute("INSERT INTO temperature (date, time, temperature) VALUES (?, ?, ?)", ("2025-01-18", "18:00", -1.0))
cursor.execute("INSERT INTO temperature (date, time, temperature) VALUES (?, ?, ?)", ("2025-01-19", "21:00", -3.3))
cursor.execute("INSERT INTO temperature (date, time, temperature) VALUES (?, ?, ?)", ("2025-01-20", "06:00", -5.0))
cursor.execute("INSERT INTO temperature (date, time, temperature) VALUES (?, ?, ?)", ("2025-01-21", "09:00", -1.8))

conn.commit()

cursor.execute("SELECT * FROM temperature")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()

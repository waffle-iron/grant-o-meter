import sqlite3
from datetime import date, datetime

conn = sqlite3.connect('grantometer.db')
c = conn.cursor()
c.execute('''CREATE TABLE grumpies (id INTEGER PRIMARY KEY, added_at DATE,
             commenter TEXT, comment TEXT, grumpyness INTEGER)''')

today = datetime.utcnow() 
c.execute('''INSERT INTO grumpies (added_at, commenter, comment, grumpyness)
             VALUES(?, ?, ?, ?)''',(today, 'commenter', 'comment' , 10))

conn.commit()

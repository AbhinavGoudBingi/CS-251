import sqlite3

conn = sqlite3.connect('pokedex.db')
c=conn.cursor()
var = c.execute('''SELECT identifier FROM POKEMON ORDER BY base_experience DESC LIMIT 3;''')
for row in var:
	print(row[0])
conn.commit()
conn.close()

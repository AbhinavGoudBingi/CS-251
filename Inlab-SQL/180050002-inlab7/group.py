import sqlite3

conn = sqlite3.connect('pokedex.db')
c=conn.cursor()
var=c.execute('''SELECT species_id,max(base_experience) FROM POKEMON GROUP BY species_id ORDER BY base_experience DESC LIMIT 3;''')
for row in var:
	print(row[1])
conn.commit()
conn.close()
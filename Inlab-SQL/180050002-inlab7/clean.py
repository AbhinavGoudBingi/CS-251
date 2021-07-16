import sqlite3

conn = sqlite3.connect('pokedex.db')
c=conn.cursor()
c.execute("DELETE FROM POKEMON WHERE identifier like 'rogue%';")
conn.commit()
conn.close()

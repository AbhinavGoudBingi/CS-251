import sqlite3
conn= sqlite3.connect('pokedex.db')
c=conn.cursor()
c.execute("UPDATE ABILITIES SET generation_id=8 WHERE is_main_series=0")
conn.commit()
conn.close()
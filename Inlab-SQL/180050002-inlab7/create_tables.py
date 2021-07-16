import sqlite3

conn = sqlite3.connect('pokedex.db')
c=conn.cursor()
c.execute('''CREATE TABLE POKEMON
         (id INT,
         identifier           TEXT,
         species_id            INT,
         height        INT,
         weight        INT,
         base_experience    INT,
         'order'  INT,
         is_default     INT);''')
c.execute('''CREATE TABLE ABILITIES
         (id INT,
         identifier           TEXT,
         generation_id            INT,
         is_main_series        INT);''')
c.execute('''CREATE TABLE POKEMON_ABILITIES
         (pokemon_id INT,
         ability_id           INT,
         is_hidden            INT,
         slot        INT);''')
conn.commit()
conn.close()
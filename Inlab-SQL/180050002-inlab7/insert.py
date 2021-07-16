import csv,sqlite3

conn = sqlite3.connect('pokedex.db')
c=conn.cursor()
with open('pokemon.csv','rt') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['id'], i['identifier'], i['species_id'], i['height'], i['weight'], i['base_experience'], i['order'], i['is_default']) for i in dr]

c.executemany("INSERT INTO POKEMON (id, identifier, species_id, height, weight, base_experience, 'order', is_default) VALUES (?, ?, ?, ?, ?, ?, ?, ?);", to_db)

with open('abilities.csv','rt') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['id'], i['identifier'], i['generation_id'], i['is_main_series']) for i in dr]

c.executemany("INSERT INTO ABILITIES (id, identifier, generation_id, is_main_series) VALUES (?, ?, ?, ?);", to_db)

with open('pokemon_abilities.csv','rt') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['pokemon_id'], i['ability_id'], i['is_hidden'], i['slot']) for i in dr]

c.executemany("INSERT INTO POKEMON_ABILITIES (pokemon_id, ability_id, is_hidden, slot) VALUES (?, ?, ?, ?);", to_db)

conn.commit()
conn.close()

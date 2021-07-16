import sqlite3
conn = sqlite3.connect('pokedex.db')
c=conn.cursor()
var = c.execute('''SELECT POKEMON_ABILITIES.pokemon_id, POKEMON_ABILITIES.ability_id, POKEMON.identifier AS pokemon_identifier, ABILITIES.identifier AS ability_identifier
FROM ((POKEMON_ABILITIES
INNER JOIN POKEMON ON POKEMON_ABILITIES.pokemon_id = POKEMON.id)
INNER JOIN ABILITIES ON POKEMON_ABILITIES.ability_id = ABILITIES.id);''')
ans={}
for h in var:
    ans.setdefault(h[2],[]).append(h[3]);
for h in ans:
    ans[h].sort()
ans=sorted(ans.items())
for h in ans:
    print("%s=[%s]"% (h[0],(','.join(h[1]))));
conn.commit()
conn.close()
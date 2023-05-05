import sqlite3
import sys
from pymongo import MongoClient
connection = sqlite3.connect("pokemon.sqlite")
con = connection.cursor()

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

for i in range(1, 802):
    pokemonRow = con.execute("SELECT * FROM pokemon WHERE id = " + str(i)).fetchone()

    pokemonType1 = con.execute("SELECT * FROM type LEFT OUTER JOIN pokemon_type ON type.id = pokemon_type.type_id WHERE pokemon_id = " 
                               + str(i) + " AND which = 1").fetchone()
    
    pokemonType2 = con.execute("SELECT * FROM type LEFT OUTER JOIN pokemon_type ON type.id = pokemon_type.type_id WHERE pokemon_id = " 
                               + str(i) + " AND which = 2").fetchone()

    pokemonAbilities = con.execute("SELECT * FROM ability LEFT OUTER JOIN pokemon_abilities ON ability.id = pokemon_abilities.ability_id WHERE pokemon_id = " 
                                    + str(i)).fetchmany(6)
    
    newAbility = []

    for j in range(len(pokemonAbilities)):
        newAbility.append(pokemonAbilities[j][1])
    
    abilities = newAbility

    pokemon = {
       "name": pokemonRow[2],
       "pokedex_number": pokemonRow[1],
       "types": [pokemonType1[1],   
                pokemonType2[1]],
       "hp": pokemonRow[5],
       "attack": pokemonRow[6],
       "defense": pokemonRow[7],
       "speed": pokemonRow[8],
       "sp_attack": pokemonRow[9],
       "sp_defense": pokemonRow[10],
       "abilities": abilities
    }

    x = pokemonColl.insert_one(pokemon)
    print(x)

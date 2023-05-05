import pymongo
import sys
from pymongo import MongoClient

from pymongo import MongoClient
mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# finding pikachu query
print("Find Pikachu!:")
print()
pikachu = pokemonColl.find_one({"name": "Pikachu"})
print(pikachu)
print()

# finding all pokemon with attack greater than 150 query 
print("All attacks greater than 150:")
print()
greaterThan = pokemonColl.find({"attack": {"$gt":150}})
for i in greaterThan:
    print(i)
print()

# finding all pokemon with ability "overgrow" query
# overgrowAbility = pokemonColl.find({"abilities": { "$all": ["Overgrow"]}})
print("All Overgrow abilities:")
print()
overgrowAbility = pokemonColl.find({"abilities": "Overgrow"})
for j in overgrowAbility:
    print(j)
print()


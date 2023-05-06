from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

count_docu = pokemonColl.count_documents({})
print("I found " + str(count_docu) + " pokemon")

pokemonDB.getCollection("pokemon_data").find({})
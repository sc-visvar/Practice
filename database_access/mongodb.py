from pymongo import MongoClient
from dotenv import load_dotenv
import os


load_dotenv()

# Create a MongoClient to the running MongoDB instance
client = MongoClient(os.getenv("MONGO_URL"))

# Access a specific database
db = client['sample_mflix']

# Access a specific collection
collection = db['comments']

# Example operation: Find one document
document = collection.find_one()
print(document)

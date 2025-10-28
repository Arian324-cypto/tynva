from pymongo import MongoClient

def get_database():
    CONNECTION_STRING = "mongodb://localhost:27017"
    client = MongoClient(CONNECTION_STRING)
    return client["tynva_db"]

if __name__ == "__main__":
    db = get_database()
    print("✅ Connected to Tynva Database:", db.name)

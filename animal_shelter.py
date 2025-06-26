from pymongo import MongoClient

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        USER = 'aacuser'
        PASS = 'AACpass123'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30467
        DB = 'AAC'
        COL = 'animals'

        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}')
        self.database = self.client[DB]
        self.collection = self.database[COL]

    def create(self, data):
        """Inserts a document into the collection."""
        if data:
            try:
                result = self.collection.insert_one(data)
                return True if result.inserted_id else False
            except Exception as e:
                print(f"Error inserting document: {e}")
                return False
        else:
            raise Exception("No data to insert")

    def read(self, query):
        """Finds documents that match the query."""
        if query is not None:
            try:
                return list(self.collection.find(query))
            except Exception as e:
                print(f"Error reading documents: {e}")
                return []
        else:
            raise Exception("No query provided")

from pymongo import MongoClient
import certifi

#Configure the connection with Mongodb
MONGO_URI = 'mongodb+srv://victor3:IceCream21@cluster0.qchzran.mongodb.net/'
ca = certifi.where()

#Function to connect to the database
def dbConnection():
    try:
        # Create a MongoDB client using the provided URI and TLS certificate
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        # Access the "dbb_products_app" database
        db = client["dbb_products_app"]
    except ConnectionError:
        # Handle connection errors
        print('Database connection error')
    return db
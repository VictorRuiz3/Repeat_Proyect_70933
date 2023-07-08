from pymongo import MongoClient
import certifi

#Configure the connection with Mongodb
MONGO_URI = 'mongodb+srv://victor3:IceCream21@cluster0.qchzran.mongodb.net/'
ca = certifi.where()

#Function to connect to the database
def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["dbb_products_app"]
    except ConnectionError:
        print('Database connection error')
    return db
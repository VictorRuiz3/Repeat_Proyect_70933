class Product:
    
    #Builder
    def __init__(self, name, price, quantity):
        # Initialize the Product object with the provided name, price, and quantity
        self.name = name
        self.price = price
        self.quantity = quantity

    #Function to save writing data
    def toDBCollection(self):
        # Convert the Product object to a dictionary format suitable for storing in a database collection
        return{
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity
        }
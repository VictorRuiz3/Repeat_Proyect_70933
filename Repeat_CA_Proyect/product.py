class Product:
    
    #Builder
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    #Function to save writing data
    def toDBCollection(self):
        return{
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity
        }
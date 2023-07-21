from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import database as dbase  
from product import Product

# Establish a connection to the database
db = dbase.dbConnection()
# Create an instance of the Flask application
app = Flask(__name__)

# Define the main path of the application
@app.route('/')
# Function to handle the home page
def home():
    # Access the 'products' collection in the database
    products = db['products']
    # Retrieve all products from the collection
    productsReceived = products.find()
    # Render the index.html template and pass the products to it
    return render_template('index.html', products = productsReceived)

# Handle the HTTP POST request to add a product
@app.route('/products', methods=['POST'])
def addProduct(name,price,quantity):
    products = db['products']
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']

    # Check if all required fields are filled
    if name and price and quantity:
        product = Product(name, price, quantity)
        # Insert the product into the collection
        products.insert_one(product.toDBCollection())
        response = jsonify({
            'name' : name,
            'price' : price,
            'quantity' : quantity
        })
        # Redirect the user to the home page
        return redirect(url_for('home'))
    else:
        # If any required field is missing, return a 404 error
        return notFound()
    
def addProducts(name,price,quantity):
    products = db['products']

    # Check if all required fields are filled
    if name and price and quantity:
        product = Product(name, price, quantity)
        # Insert the product into the collection
        products.insert_one(product.toDBCollection())
        response = jsonify({
            'name' : name,
            'price' : price,
            'quantity' : quantity
        })
        # Redirect the user to the home page
        return redirect(url_for('home'))
    else:
        # If any required field is missing, return a 404 error
        return notFound()
        

# Handle the HTTP DELETE request to remove a product
@app.route('/delete/<string:product_name>')
def delete(product_name):
    # Access the 'products' collection in the database
    products = db['products']
    # Delete the product with the specified name from the collection
    products.delete_one({'name' : product_name})
    # Redirect the user to the home page
    return redirect(url_for('home'))

# Handle the HTTP PUT request to edit a product
@app.route('/edit/<string:product_name>', methods=['POST'])
def edit(product_name):
    # Access the 'products' collection in the database
    products = db['products']
    # Retrieve the updated product details from the form data
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']

    # Check if all required fields are filled
    if name and price and quantity:
        # Update the product with the specified name in the collection
        products.update_one({'name' : product_name}, {'$set' : {'name' : name, 'price' : price, 'quantity' : quantity}})
        # Create a JSON response with a success message
        response = jsonify({'message' : 'Product ' + product_name + ' updated successfully'})
        # Redirect the user to the home page
        return redirect(url_for('home'))
    else:
        # If any required field is missing, return a 404 error
        return notFound()

# Handle the 404 error
@app.errorhandler(404)
def notFound(error=None):
    # Create a JSON response with a not found message and status code
    message ={
        'message': 'Not found ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response

# Run the application on the specified port with debug mode enabled
if __name__ == '__main__':
    app.run(debug=True, port=4000)

def helloworld():
    return "hello-world"
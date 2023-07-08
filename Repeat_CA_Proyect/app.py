from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import database as dbase  
from product import Product

db = dbase.dbConnection()

app = Flask(__name__)

#Application main path
@app.route('/')
#Function to start the application
def home():
    products = db['products']
    productsReceived = products.find()
    return render_template('index.html', products = productsReceived)

#Method Post, to add the products to the database
@app.route('/products', methods=['POST'])
def addProduct():
    products = db['products']
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']

    if name and price and quantity:
        product = Product(name, price, quantity)
        products.insert_one(product.toDBCollection())
        response = jsonify({
            'name' : name,
            'price' : price,
            'quantity' : quantity
        })
        return redirect(url_for('home'))
    else:
        return notFound()

#Method delete, to remove the products from the database
@app.route('/delete/<string:product_name>')
def delete(product_name):
    products = db['products']
    products.delete_one({'name' : product_name})
    return redirect(url_for('home'))

#Method Put, to edit the products in the database
@app.route('/edit/<string:product_name>', methods=['POST'])
def edit(product_name):
    products = db['products']
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']

    if name and price and quantity:
        products.update_one({'name' : product_name}, {'$set' : {'name' : name, 'price' : price, 'quantity' : quantity}})
        response = jsonify({'message' : 'Product ' + product_name + ' updated successfully'})
        return redirect(url_for('home'))
    else:
        return notFound()

#Function in case there is an error
@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'Not found ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response

#Define the port where to execute and activate the debug
if __name__ == '__main__':
    app.run(debug=True, port=4000)
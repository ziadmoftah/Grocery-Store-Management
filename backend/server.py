from flask import Flask, jsonify, request
import products_dao
from sql_connection import get_sql_connection
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
connection = get_sql_connection()

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/getAllProducts' , methods = ['GET'])
def getProducts():
    products = products_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/deleteProduct' , methods = ['POST'])
def deleteProduct():
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id' : return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
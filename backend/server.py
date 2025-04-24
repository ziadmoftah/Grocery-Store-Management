from flask import Flask, jsonify, request
import json
import products_dao, measurement_units_dao, orders_dao
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

@app.route('/getUnitsName', methods = ['GET'])
def getUnitsName():
    unitsName = measurement_units_dao.get_units_name(connection)
    response = jsonify(unitsName)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertProduct' , methods = ['POST'])
def insertProduct():
    request_payload = json.loads(request.form['data'])
    print (request_payload)
    product_id = products_dao.insert_new_product(connection, request_payload)
    response = jsonify({'product_id' : product_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/editProductPrice' , methods = ['POST'])
def editProductPrice():
    response = jsonify({'product_id': products_dao.edit_product_price(connection , request.form['id'] , request.form['new_price'])})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route ('/insertOrder' , methods = ['POST'])
def insertOrder():
    order_data = json.loads(request.form['data'])
    order_id = orders_dao.insert_order(connection, order_data)
    response = jsonify({'order_id' : order_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route ('/getAllOrders' , methods = ['GET'])
def getAllOrders():
    order_details = orders_dao.get_all_orders(connection)
    response = jsonify(order_details)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
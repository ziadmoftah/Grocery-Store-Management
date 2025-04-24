from sql_connection import get_sql_connection
from datetime import datetime

def insert_order(connection , order):
    cursor = connection.cursor()
    query = ('INSERT INTO grocery_store.order ( customer_name, total_price, time_of_purchase) '
             'VALUES ( %s , %s , %s )')
    order_data = ( order['customer_name'] , order['grand_total'] , str(datetime.now()) )
    order_product_details = order['order_details']
    cursor.execute(query, order_data )
    connection.commit()
    order_id = cursor.lastrowid
    insert_order_product_details(connection, order_product_details , order_id)
    return order_id

def insert_order_product_details(connection , order_products_details , order_id):
    cursor = connection.cursor()
    query = ('INSERT INTO order_details (`order_id`, `product_id`, `quantity`, `total_price`) '
             'VALUES (%s, %s, %s, %s)')
    product_detail_object = []
    for product in order_products_details:
        product_detail_object.append((order_id , product['product_id'] , product['quantity'], product['total_price']))
    cursor.executemany(query, product_detail_object)
    connection.commit()

def get_all_orders(connection):
    cursor = connection.cursor()
    query = ('SELECT order_id, customer_name, total_price, time_of_purchase '
             'FROM grocery_store.order')
    cursor.execute(query)
    order_details = []
    for (order_id, customer_name, total_price, time_of_purchase) in cursor:
        order_details.append({
            'order_id' : order_id,
            'customer_name' : customer_name,
            'total_price' : total_price,
            'time_of_purchase' : time_of_purchase
        })
    return order_details

if __name__ == "__main__":
    sql_connection = get_sql_connection()
    orders = get_all_orders(sql_connection)
    for x in orders:
        print(x)

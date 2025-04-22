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

def insert_order_product_details(connection , order_products_details , order_id):
    cursor = connection.cursor()
    query = ('INSERT INTO order_details (`order_id`, `product_id`, `quantity`, `total_price`) '
             'VALUES (%s, %s, %s, %s)')
    product_detail_object = []
    for product in order_products_details:
        product_detail_object.append((order_id , product['product_id'] , product['quantity'], product['total_price']))
    cursor.executemany(query, product_detail_object)
    connection.commit()

if __name__ == "__main__":
    sql_connection = get_sql_connection()

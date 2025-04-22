from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()
    query = ("Select p.product_id, p.name, u.name, p.price_per_unit, u.unit_id "
             "from product p "
             "JOIN unit_of_measurement u "
             "on u.unit_id = p.unit_id")
    cursor.execute(query)
    response = []
    for (product_id , product_name, unit_name , price_per_unit, unit_id) in cursor:
        response.append({
            'product_id' : product_id,
            'product_name': product_name,
            'unit_name' : unit_name,
            'price_per_unit' : price_per_unit,
            'unit_id' : unit_id
        })

    return response


def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO product "
             "(name, unit_id, price_per_unit) "
             "VALUES ( %s , %s , %s )")

    product_data = ( product['product_name'] , product['product_unit_id'] , product['product_price_per_unit'])
    cursor.execute(query , product_data)
    connection.commit()
    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM product "
             "WHERE product_id = "+ str(product_id) )
    cursor.execute(query)
    connection.commit()
    return str(product_id)

def edit_product_price(connection, product_id, new_price):
    cursor = connection.cursor()
    query = ("UPDATE product"
             " SET `price_per_unit` = " +str(new_price)+
             " WHERE (`product_id` ="+str(product_id)+")")
    cursor.execute(query)
    connection.commit()
    return product_id

if __name__ == "__main__":
    sql_connection = get_sql_connection()
    edit_product_price(sql_connection , 1 , 15)

    product = get_all_products(sql_connection)
    for x in product:
        print(x)

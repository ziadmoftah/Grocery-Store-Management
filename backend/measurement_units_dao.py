from sql_connection import get_sql_connection

def get_units_name(connection):
    cursor = connection.cursor()
    query = ('SELECT unit_id , name '
             'FROM unit_of_measurement')
    cursor.execute(query)
    response = []
    for (unit_id , unit_name) in cursor:
        response.append({
            'unit_id' : unit_id,
            'unit_name' : unit_name
        })
    return response
import psycopg2 as pg

def estimated_time_by_product():
    conn = pg.connect(database="orbidi", user="postgres", password="password", host="localhost", port="5432")
    cursor = conn.cursor()

    # This query returns the sum of time_estimate grouped by Product
    sql_query = """
        SELECT producto, SUM((data->>'time_estimate')::bigint) as total_estimated_time
        FROM proyectos
        GROUP BY producto;
    """

    cursor.execute(sql_query)
    results = cursor.fetchall()

    print("Tiempo estimado total en horas por tipo de producto:")
    for product, total_estimated_time in results:
        print(f"Producto {product}: {total_estimated_time / (60 * 60 * 1000)} horas")

    #Saving the data in a new table
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS tiempo_por_producto AS
            SELECT producto, SUM((data->>'time_estimate')::bigint)/ (60*60*1000) as total_estimated_time_in_hours
            FROM proyectos
            GROUP BY producto;
       """)

    conn.commit()
    cursor.close()
    conn.close()

estimated_time_by_product()
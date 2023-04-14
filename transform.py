import psycopg2 as pg
import re

def get_product_value(name, product_map):
    #Extracting product type using Regex
    match = re.search("[A-Za-z]+-[A-Za-z]+",name)
    if match:
        product_key = match.group()
    return product_map.get(product_key)

product_map = {
        "KD-WEB": 0,
        "KD-SEO": 1,
        "KD-ANALITICA": 2,
        "KD-RRSS": 3,
        "KD-ECOMMERCE": 4,
        "KD-CRM": 5,
        "KD-PROC": 6,
        "KD-FACT": 7,
    }


#Get the projects from DB
conn = pg.connect(database="orbidi", user="postgres", password="password", host="localhost", port="5432")
cursor = conn.cursor()

#Creating new Column called 'Producto'
cursor.execute("ALTER TABLE proyectos ADD COLUMN IF NOT EXISTS producto INT;")

#Get data from BD
cursor.execute("SELECT id, data FROM proyectos;")
project_data = cursor.fetchall()

# Actualizar la columna 'producto' en la base de datos
for project_id, data in project_data:
    product_value = get_product_value(data["name"], product_map)

    cursor.execute("UPDATE proyectos SET producto = %s WHERE id = %s;", (product_value, project_id))

conn.commit()
cursor.close()
conn.close()
#Import libraries to use
import requests
import json
import psycopg2 as pg

API = "pk_3041236_DXOBGO4W2M220TSFKLKVFUDZ50WP4VG9"
HEADERS = {"Authorization": API}

#Connecting to PostgreSQL
conn = pg.connect(database="orbidi", user="postgres", password="password", host="localhost", port="5432")
cursor = conn.cursor()

#Function to get the data from API
def connection(list_id):
    url = f"https://api.clickup.com/api/v2/list/{list_id}/task"
    response = requests.get(url, headers=HEADERS)
    return response.json()["tasks"]

#Create tables in DB
cursor.execute("""CREATE TABLE IF NOT EXISTS clientes (id SERIAL PRIMARY KEY, data JSONB);""")
cursor.execute("""CREATE TABLE IF NOT EXISTS proyectos (id SERIAL PRIMARY KEY, data JSONB);""")

#Extracting data
list_id = {"clientes": 900100953154, "proyectos": [900100953291, 900100953296, 900100953297]}
tasks = {"clientes": connection(list_id["clientes"]), "proyectos": []}

for proyecto_list_id in list_id["proyectos"]:
    tasks["proyectos"].extend(connection(proyecto_list_id))

#Inserting data into DB
for cliente in tasks["clientes"]:
    cursor.execute("INSERT INTO clientes (data) VALUES (%s);", (json.dumps(cliente),))
for proyecto in tasks["proyectos"]:
    cursor.execute("INSERT INTO proyectos (data) VALUES (%s);", (json.dumps(proyecto),))

conn.commit()
cursor.close()
conn.close()



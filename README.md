# ETL with ClickUP API

En este proyecto se implementa un proceso ETL utilizando Python y PostgreSQL para extraer información de entidades de Cliente y Proyecto de una API de ClickUP

## Requisitos

- Python 3.6+
- pip
- psycopg2
- PostgreSQL

## Configuración

1. Cree un entorno virtual 'venv' con pip y activarlo:

`python3 -m venv venv`
`source venv/bin/activate`

o en Windows:

`.\venv\Scripts\activate`


2. Instale las dependencias:

`pip install psycopg2`
`pip install requests`

3. Tener una base de datos PostgreSQL en local disponible con la siguiente configuracion:
`database="orbidi", user="postgres", password="password", host="localhost", port="5432"`
En caso de ya contar con una BD, modificar las variables de conexion.

4. Ejecute los scripts de Python en el siguiente orden:

- extract.py
- transform.py
- load.py

Cada script de Python se enfoca en una etapa del proceso ETL:

- extract.py: extrae información de las entidades Cliente y Proyecto utilizando la API de ClickUp y guarda los datos en una base de datos PostgreSQL.
- transform.py: realiza transformaciones en los datos extraídos.
- load.py: calcula la suma del tiempo estimado agrupado por tipo de producto.

## Ejecución

Para ejecutar cada script, simplemente ejecute el siguiente comando:

`python script_name.py`

Reemplace "script_name.py" con el nombre del script que desea ejecutar.

Después de ejecutar los scripts en orden, podrá ver los resultados el la BD.

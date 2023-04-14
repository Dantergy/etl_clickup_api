# Orbidi Take home challenge

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

## Respuesta a preguntas
1- Considerando que actualmente tenemos 1.000 clientes en nuestro entorno de
ClickUp de producción y que nos gustaría disponer de la información con la máxima
rapidez posible en nuestro entorno de explotación de datos. ¿Cómo plantearías la
estrategia de extracción para conseguirlo? ¿Qué retos anticipas? ¿Qué
consideraciones deberíamos tomar?

##### R// Una estrategia es implementar procesos de extraccion en paralelo usando herramientas como Airflow lo que permitiria obtener multiples datos de manera simultanea.  El reto seria evaluar los limites del API de ClickUp en cuanto a concurrencia. 

2-  Considerando que utilizamos un segundo sistema HubSpot dónde tenemos toda la
información de Clientes (es la verdadera base de clientes - source of truth - ). Nos
gustaría también relacionar la información de esa segunda fuente de datos con la
herramienta de gestión de clientes Clickup y sus respectivas entidades (clientes).
¿Qué estrategia consideras que deberíamos seguir? ¿Cómo resolverías el caso en
el cual en Hubspot la información de un cliente aparezca distinta que en ClickUp?

##### R // La estrategia en este caso, seria tener un tipo de 'Key' que permita relacionar la informacion entre ambos datos, esa key puede ser el Email o un Documento de identidad, en caso de informacion diferente entre ambas plataformas, es necesario crear un proceso de Data quality, en el que se puede implementar priorizacion sobre una fuente de datos por ejemplo.

3-  ¿Cómo harías que este proceso se ejecute de forma periódica?

##### R // Una opcion adecuada es implementando los ETL en un servicio como Airflow que tenga una orden de ejecución.

4-  ¿Qué método implementarías para detectar errores en el proceso y cómo
asegurarías su consistencia?

##### R // Se implementaria un proceso de Data quality, que en caso de detectar un error en los datos notifique por diversos medios (Slack, Email), para proceder a verificar y solucionar el error.

5-  ¿Cómo harías una integración entre ClickUp y HubSpot para sincronizar la
información (estados de proyectos, pagos, etc) entre ambas plataformas en tiempo
real (o con una frecuencia considerablemente alta)?

##### R // Implementando Webhooks o eventos que notifiquen modificaciones o cambios en alguna ClickUp y HubSpot, por medio de esos eventos se implementa un servicio que este escuchando y ejecute los jobs necesarios.
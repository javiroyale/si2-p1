# connect to the database , read the first 1000 entries
# then perform 1000 queries retrieving each one of the entries
# one by one . Measure the time requiered for the 1000
import django
import psycopg2
import time

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "visaSite.settings")
django.setup()

from visaAppWSBackend.models import Tarjeta

db_config = {
'dbname': 'si2db', # Nombre de la base de datos
'user': 'alumnodb', # Reemplaza con tu usuario de PostgreSQL
'password': 'alumnodb', # Reemplaza con tu contrasegna 
'host': 'localhost', # Cambia si el host es diferente
'port': 15432 , # Cambia si tu puerto es diferente
}
try :
    # Conexion a la base de datos
    conn = psycopg2.connect(** db_config )
    cursor = conn.cursor ()

    tarjetas = list(Tarjeta.objects.all()[:1000])
    
    start_time = time.time ()
    
    for tarjeta in tarjetas:
        Tarjeta.objects.get(numero=tarjeta.numero)

    end_time = time.time ()

    print (f" Tiempo invertido en buscar las 1000 entradas una a una : { end_time - start_time :.6f}, segundos ")

except Exception as e:
    print(f"Error: {e}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
    

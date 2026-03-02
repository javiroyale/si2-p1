# Uses rabbitMQ as the server
import os
import sys
import django
import pika

BASE_DIR = os . path . dirname (
    os . path . dirname ( os . path . abspath ( __file__ )) )

sys . path . append ( BASE_DIR )

os . environ . setdefault ('DJANGO_SETTINGS_MODULE',
    'visaSite.settings')

django.setup ()

from visaAppRPCBackend . models import Tarjeta , Pago

def main () :
    if len ( sys . argv ) != 3:
        print (" Debe indicar el host y el puerto ")
        exit () 
    hostname = sys . argv [ 1 ]
    port = sys . argv [ 2 ]

    credenciales = pika.PlainCredentials('alumnomq', 'alumnomq')

    params = pika.ConnectionParameters(host=hostname, port=port, credentials=credenciales)

    try:
        #conexión síncrona que espera respuesta del server antes de continuar su ejecución, 
        # el hilo del cliente será bloqueado hasta que el server responda
        pbc = pika.BlockingConnection(params)  
        canal = pbc.channel()
        #creamos la cola
        canal.queue_declare(queue='pago_cancelacion')

        #registramos la funcion de callback en la cola
        canal.basic_consume(
                queue='pago_cancelacion',
                on_message_callback=procesar_mensajes,
                auto_ack=True  
        )

        #consumición de mensajes, se bloquea el hilo
        canal.start_consuming()
    
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        if 'pbc' in locals() and pbc.is_open:
            pbc.close()




def procesar_mensajes(ch, method, properties, body):
    #los params (body) llega en Bytes ???, pasamos a string y solo me llega el idPago
    idPago = body.decode()

    try:
        pago = Pago.objects.get(id=idPago)
        
        pago.codigoRespuesta = '111'
        pago.save()
        
        print(f" [V] Pago {idPago} cancelado satisfactoriamente (Código 111).")
    
    except Pago.DoesNotExist:
        print(f"El pago no existe, id: {idPago}")
        return False
    except Exception as e:
        print(f"ERROR: {e}")
        return False

    print(f"Pago con id: {idPago} cancelado")
    return True


if __name__ == '__main__':
    main ()
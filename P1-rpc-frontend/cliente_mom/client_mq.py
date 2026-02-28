import pika
import sys

def cancelar_pago(hostname, port, id_pago):

    hostname = sys.argv[1]
    port = int(sys.argv[2])
    id_pago = sys.argv[3]

    credenciales = pika.PlainCredentials('alumnomq', 'alumnomq')

    params = pika.ConnectionParameters(
        host=hostname, 
        port=port, 
        credentials=credenciales
    )

    try:
        pbc = pika.BlockingConnection(params)  
        canal = pbc.channel()
    except Exception as e:
        print("Error al conectar al host remoto")
        exit()
    
    canal.queue_declare(queue='pago_cancelacion')   

    #publicamos en el canal el pago a cancelar
    canal.basic_publish(
            exchange='',           
            routing_key='pago_cancelacion', 
            body=id_pago           
    )
    
    pbc.close()

def main():
    if len(sys.argv) != 4:
        print("Debe indicar el host, el numero de puerto y el ID del pago a cancelar como argumento.")
        exit()
    
    cancelar_pago(sys.argv[1], sys.argv[2], sys.argv[3])


if __name__ == "__main__":
    main()
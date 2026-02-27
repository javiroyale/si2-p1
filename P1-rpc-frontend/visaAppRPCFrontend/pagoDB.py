from django.conf import settings
from xmlrpc.client import ServerProxy

def verificar_tarjeta(tarjeta_data):
    """ 
    Verifica si una tarjeta está registrada en el sistema remoto.
    
    :param tarjeta_data: dict - Diccionario con los datos de la tarjeta (procedente de TarjetaForm).
    :return: bool - True si la tarjeta es válida y está registrada, False en caso contrario.
    """
    with ServerProxy(settings.RPCAPIBASEURL) as proxy:
        return proxy.verificar_tarjeta(tarjeta_data)


def registrar_pago(pago_dict):
    """ 
    Registra un nuevo pago en la base de datos remota.
    
    :param pago_dict: dict - Datos del pago e incluye el ID de la tarjeta.
    :return: dict/None - Información del pago recién creado si tiene éxito; None si falla.
    """
    with ServerProxy(settings.RPCAPIBASEURL) as proxy:
        return proxy.registrar_pago(pago_dict)


def eliminar_pago(idPago):
    """ 
    Elimina un registro de pago específico mediante su identificador.
    
    :param idPago: int - El identificador único del pago a borrar.
    :return: bool - True si la eliminación fue exitosa, False si hubo error o no existía.
    """
    with ServerProxy(settings.RPCAPIBASEURL) as proxy:
        return proxy.eliminar_pago(idPago)


def get_pagos_from_db(idComercio):
    """ 
    Recupera la lista de pagos asociados a un comercio específico.
    
    :param idComercio: str - Identificador del comercio.
    :return: list - Una lista de diccionarios, donde cada uno representa un pago encontrado.
    """
    with ServerProxy(settings.RPCAPIBASEURL) as proxy:
        return proxy.get_pagos_from_db(idComercio)

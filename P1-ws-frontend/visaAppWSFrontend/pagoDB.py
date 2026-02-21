# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# author: rmarabini
"Interface with the dataabse"


from django.conf import settings
import requests


def verificar_tarjeta(tarjeta_data):
    """ Check if the tarjeta is registered 
    :param tarjeta_dict: dictionary with the tarjeta data
                       (as provided by TarjetaForm)
    :return True or False if tarjeta_data is not valid
    """
    api_url = settings.RESTAPIBASEURL + "tarjeta/"
    response = requests.post(api_url, tarjeta_data)
    if response.status_code == 200:
        return True
    return False

def registrar_pago(pago_dict):
    """ Register a payment in the database
    :param pago_dict: dictionary with the pago data (as provided by PagoForm)
      plus de tarjeta_id (numero) of the tarjeta
    :return new pago info if succesful, None otherwise
    """
    
    api_url = settings.RESTAPIBASEURL + "pago/"
    response = requests.post(api_url, pago_dict)
    if response.status_code == 200:
        pago = response.json()
        return pago
    raise Exception(response.text)


def eliminar_pago(idPago):
    """ Delete a pago in the database
    :param idPago: id of the pago to be deleted
    :return True if succesful,
     False otherwise
     """
    d={"idPago":idPago}
    api_url = settings.RESTAPIBASEURL + "pago/" + str(idPago) + "/"
    response = requests.delete(api_url)
    if response.status_code == 200:
        return True
    return False



def get_pagos_from_db(idComercio):
    """ Gets pagos in the database correspondint to some idComercio
    :param idComercio: id of the comercio to get pagos from 
    :return list of pagos found
     """
    api_url = settings.RESTAPIBASEURL + "comercio/" + str(idComercio) + "/"
    pagos = requests.get(api_url, idComercio)
    return pagos

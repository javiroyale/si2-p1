from rest_framework import serializers
from visaAppWSBackend.models import Pago, Tarjeta


class PagoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = [
            'id', 'idComercio', 'idTransaccion', 
            'importe', 'tarjeta', 'marcaTiempo', 
            'codigoRespuesta'  
        ]


class TarjetaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = [
            'id', 'numero', 'nombre',
             'fechaCaducidad', 'codigoAutorizacion'
        ]
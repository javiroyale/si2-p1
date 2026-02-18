from rest_framework import serializers
from visaAppWSBackend.models import Pago, Tarjeta


class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = [
            'id', 'idComercio', 'idTransaccion', 
            'importe', 'tarjeta', 'marcaTiempo', 
            'codigoRespuesta'  
        ]


class TarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = [
            'numero', 'nombre',
             'fechaCaducidad', 'codigoAutorizacion'
        ]
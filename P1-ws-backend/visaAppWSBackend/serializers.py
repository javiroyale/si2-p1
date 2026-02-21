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
        read_only_fields = [
            'marcaTiempo', 'codigoRespuesta'
        ]


class TarjetaSerializer(serializers.ModelSerializer):
    numero = serializers.CharField(max_length=19)
    class Meta:
        model = Tarjeta
        fields = [
            'numero', 'nombre',
             'fechaCaducidad', 'codigoAutorizacion'
        ]
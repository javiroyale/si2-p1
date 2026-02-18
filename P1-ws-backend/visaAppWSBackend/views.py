from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pago, Tarjeta
from .serializers import PagoSerializer, TarjetaSerializer
from .pagoDB import verificar_tarjeta, registrar_pago, eliminar_pago, get_pagos_from_db

class TarjetaView(APIView):

    def post(self, request):

        datos = request.data

        serializer = TarjetaSerializer(data=datos)
        if serializer.is_valid():
            if verificar_tarjeta(serializer.validated_data): 
                return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response({'message': 'Datos no encontrados en la base de datos'}, status=status.HTTP_404_NOT_FOUND)


class PagoView(APIView):

    def post(self, request):

        datos = request.data

        serializer = PagoSerializer(data=datos)
        if serializer.is_valid():
            data = serializer.validated_data
            if verificar_tarjeta({'numero': data['tarjeta'].numero}):
                pago = registrar_pago(data)
            else:
                return Response({'message': 'Error al registrar pago, tarjeta no existente.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'message': 'Error al registrar pago.'}, status=status.HTTP_400_BAD_REQUEST)

        if pago is None:
            return Response({'message': 'Error al registrar pago.'}, status=status.HTTP_404_NOT_FOUND)
        pago_dict = model_to_dict(pago)

        return Response(pago_dict, status=status.HTTP_200_OK)
    

    def delete(self, request, id_pago):

        if eliminar_pago(id_pago):
            return Response(status=status.HTTP_200_OK)

        return Response({'message': 'No se pudo borrar el pago.'}, status=status.HTTP_404_NOT_FOUND)


class ComercioView(APIView):

    def get(self, request, idComercio): #se pasa por aqui el idComercio porque esta en la url

        pagos = get_pagos_from_db(idComercio)
        if not pagos:
            return Response({'message': 'Error al listar los comercios'}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = PagoSerializer(pagos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
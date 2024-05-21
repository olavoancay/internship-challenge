from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import math

def mmc(a, b):
    return abs(a * b) // math.gcd(a, b)

def calcula_mmc_intervalo(inicio, fim):
    intervalo = range(inicio, fim + 1)
    resultado = intervalo[0]
    for valor in intervalo[1:]:
        resultado = mmc(resultado, valor)
    return resultado

@api_view(['GET'])
def calcula_mmc_intervalo_api(request):
    try:
        x = int(request.query_params.get('x'))
        y = int(request.query_params.get('y'))
        if x <= 0 or y <= 0:
            return Response({'error': 'Os dois números devem ser inteiros positivos'}, status=status.HTTP_400_BAD_REQUEST)
        resultado = calcula_mmc_intervalo(x, y)
        return Response({'result': resultado})
    except (TypeError, ValueError):
        return Response({'error': 'Valor inválido. Os valores de início e fim devem ser inteiros'}, status=status.HTTP_400_BAD_REQUEST)
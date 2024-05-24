from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .calculadora_mmc import CalculadoraMMC
from .validators import valida_entradas

@api_view(['GET'])
def calcula_mmc_intervalo_api(request):
    x = request.query_params.get('x')
    y = request.query_params.get('y')
    validation_error = valida_entradas(x, y)
    if validation_error:
        return validation_error
    
    x = int(x)
    y = int(y)
    calculadora = CalculadoraMMC(x, y)
    resultado = calculadora.calcula_mmc_intervalo()
    return Response({'result': resultado})


from rest_framework.response import Response
from rest_framework import status

def validate_inputs(x, y):
    try:
        x = int(x)
        y = int(y)
        if x <= 0 or y <= 0 or x >= y:
            return Response({'error': 'Os dois números devem ser inteiros positivos e x deve ser menor que y'}, status=status.HTTP_400_BAD_REQUEST)
        return None
    except (TypeError, ValueError):
        return Response({'error': 'Valor inválido. Os valores de início e fim devem ser inteiros'}, status=status.HTTP_400_BAD_REQUEST)

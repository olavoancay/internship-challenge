from rest_framework.response import Response
from rest_framework import status

# X e Y são valores recebidos como entrada dos usuários
# X determina o valor inicial do intervalo
# Y determina o valor final do intervalo
# Requisitos X e Y  
   # X e Y devem ser 2 inteiros positivos
   # X != Y
   # X < Y 


def valida_entradas(x, y):
    if not x or not y:
        return Response({'error': 'Valor inválido! Por favor, complete todos os campos do formulário'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        x = int(x)
        y = int(y)
        if x <= 0 or y <= 0:
            return Response({'error': 'Valor inválido! Por favor, digite 2 números inteiros positivos'}, status=status.HTTP_400_BAD_REQUEST)
        if x >= y:
            return Response({'error': 'Valor inválido! O valor final do intervalo deve ser maior do que o valor inicial'}, status=status.HTTP_400_BAD_REQUEST)
        return None
    except ValueError:
        return Response({'error': 'Valor inválido! Por favor, digite 2 números inteiros positivos'}, status=status.HTTP_400_BAD_REQUEST)
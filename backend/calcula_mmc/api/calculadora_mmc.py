import math

class CalculadoraMMC:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def calcula_mmc(self, a, b):
        return abs(a * b) // math.gcd(a, b)

    #REGRA DE NEGÓCIO
    #Calcula Mínimo Múltiplo Comum entre todos os números dentro de um intervalo
    #Valores de início e fim do intervalo são dados como entrada pelo usuário
    #Retorna um número inteiro que será divisível por cada um dos números do intervalo
    
    def calcula_mmc_intervalo(self):
        intervalo = range(self.inicio, self.fim + 1)
        resultado = intervalo[0]
        for valor in intervalo[1:]:
            resultado = self.calcula_mmc(resultado, valor)
        return resultado
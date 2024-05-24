import math

class CalculadoraMMC:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def calcula_mmc(self, a, b):
        return abs(a * b) // math.gcd(a, b)

    def calcula_mmc_intervalo(self):
        intervalo = range(self.start, self.end + 1)
        resultado = intervalo[0]
        for valor in intervalo[1:]:
            resultado = self.calcula_mmc(resultado, valor)
        return resultado

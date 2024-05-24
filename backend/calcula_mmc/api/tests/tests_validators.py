import unittest
from rest_framework import status
from api.validators import valida_entradas
from api.calculadora_mmc import CalculadoraMMC

class TestValidators(unittest.TestCase):
    def test_campos_em_branco(self):
        response = valida_entradas('', '')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Valor inválido! Por favor, complete todos os campos do formulário')

    def test_x_campo_em_branco(self):
        response = valida_entradas('', '10')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Valor inválido! Por favor, complete todos os campos do formulário')

    def test_y_campo_em_branco(self):
        response = valida_entradas('10', '')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Valor inválido! Por favor, complete todos os campos do formulário')

    def test_x_nao_inteiro(self):
        response = valida_entradas('abc', '10')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Valor inválido! Por favor, digite 2 números inteiros positivos')

    def test_y_nao_inteiro(self):
        response = valida_entradas('10', 'abc')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Valor inválido! Por favor, digite 2 números inteiros positivos')

    def test_x_negativo(self):
        response = valida_entradas('-1', '10')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Valor inválido! Por favor, digite 2 números inteiros positivos')

    def test_y_negativo(self):
        response = valida_entradas('10', '-1')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Valor inválido! Por favor, digite 2 números inteiros positivos')

    def test_y_menor_que_x(self):
        response = valida_entradas('10', '5')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Valor inválido! O valor final do intervalo deve ser maior do que o valor inicial')

    def test_x_igual_a_y(self):
        response = valida_entradas('10', '10')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Valor inválido! O valor final do intervalo deve ser maior do que o valor inicial')

    def test_sucesso(self):
        # Validando a entrada
        validation_error = valida_entradas('1', '10')
        self.assertIsNone(validation_error)

        # Calculando o resultado
        calculadora = CalculadoraMMC(1, 10)
        resultado = calculadora.calcula_mmc_intervalo()
        self.assertEqual(resultado, 2520)

if __name__ == '__main__':
    unittest.main()

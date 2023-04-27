import unittest
from calculos import *


class TesteMultiplicacao(unittest.TestCase):

    def teste_mult(self):
        """
        Teste unitário de multiplicação.
        :return: 0
        """
        resultado = Calculadora.multiplicar(-2, 3)
        self.assertEqual(resultado, -6)

    def teste_mult2(self):
        """
        Teste unitário de multiplicação.
        :return: 0
        """
        resultado = Calculadora.multiplicar(2, 3)
        self.assertEqual(resultado, 6)

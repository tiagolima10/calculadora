import unittest
from calculos import *


class TesteSubtracao(unittest.TestCase):

    def teste_subtrair(self):
        """
        Teste unitário de subtração.
        :return: 0
        """
        resultado = Calculadora.subtrair(2, 3)
        self.assertEqual(resultado, -1)

    def teste_subtrair2(self):
        """
        Teste unitário de subtração.
        :return: 0
        """
        resultado = Calculadora.subtrair(6, 3)
        self.assertEqual(resultado, 3)
import unittest
from calculos import *


class TesteSoma(unittest.TestCase):

    def teste_soma(self):

        """
        Teste unitário de soma.
        :return: 0
        """
        resultado = Calculadora.somar(-2, 3)
        self.assertEqual(resultado, 1)

    def teste_soma2(self):
        """
        Teste unitário de soma.
        :return: 0
        """
        resultado = Calculadora.somar(2, -3)
        self.assertEqual(resultado, -1)

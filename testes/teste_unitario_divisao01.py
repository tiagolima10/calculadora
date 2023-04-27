import unittest
from calculos import *


class TesteDivisao(unittest.TestCase):

    def teste_divisao(self):
        """
        Teste unitário de divisão.
        :return: 0
        """
        resultado = Calculadora.dividir(27, 3)
        self.assertEqual(resultado, 9)

    def teste_divisao2(self):
        """
        Teste unitário de divisão.
        :return: 0
        """
        resultado = Calculadora.dividir(2, 5)
        self.assertEqual(resultado, 0.4)
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

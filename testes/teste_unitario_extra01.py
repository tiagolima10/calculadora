import unittest
from calculos import *


class TesteDivisao(unittest.TestCase):
    def teste_divisao_por_zero(self):
        """
        Teste de integração para descobrir se foi inserido um valor 0 como segundo parâmetro.
        :return: 0
        """
        calculadora = Calculadora()

        with self.assertRaises(ZeroDivisionError):
            calculadora.dividir(27, 0)


class TesteIntegracao(unittest.TestCase):
    """
    Teste que verifica se a função somar retorna o resultado esperado quando é chamada duas vezes consecutivas.
    """
    def teste_soma_dupla(self):
        calculadora = Calculadora()

        resultado1 = calculadora.somar(2, 3)
        resultado2 = calculadora.somar(resultado1, 4)

        self.assertEqual(resultado1, 5)
        self.assertEqual(resultado2, 9)

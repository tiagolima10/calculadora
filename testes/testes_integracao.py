from teste_unitario_divisao01 import *
from teste_unitario_soma01 import *
from teste_unitario_subtracao01 import *
from teste_unitario_multiplicacao01 import *


def suite_teste():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TesteSoma))
    test_suite.addTest(unittest.makeSuite(TesteSubtracao))
    test_suite.addTest(unittest.makeSuite(TesteDivisao))
    test_suite.addTest(unittest.makeSuite(TesteMultiplicacao))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite_teste())


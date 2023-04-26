class Calculadora:
    @staticmethod
    def multiplicar(a, b):
        """
        Método que multiplica dois valores inseridos como parâmetros.
        :param a:Primeiro número parâmetro.
        :param b:Segundo número parâmetro.
        :return:Resultado da multiplicação.
        """
        resultado = a * b
        return resultado

    @staticmethod
    def dividir(a, b):
        """
        Método que divide dois valores inseridos como parâmetros.
        :param a:Primeiro número parâmetro.
        :param b:Segundo número parâmetro.
        :return:Resultado da divisão.
        """
        resultado = a / b
        return resultado

    @staticmethod
    def subtrair(a, b):
        """
        Método que subtrai dois valores inseridos como parâmetros.
        :param a:Primeiro número parâmetro.
        :param b:Segundo número parâmetro.
        :return:Resultado da subtração.
        """
        resultado = a - b
        return resultado

    @staticmethod
    def somar(a, b):
        """
        Método que multiplica dois valores inseridos como parâmetros.
        :param a:Primeiro número parâmetro.
        :param b:Segundo número parâmetro.
        :return:Resultado da soma.
        """
        resultado = a + b
        return resultado

    @staticmethod
    def calcular():
        """
        Método que faz os cálculos da calculadora.
        :return: 0
        """
        while True:
            opcao = input('Deseja continuar? Se não, digite 0:\n'
                          'Se sim, digite outro caractere: ')
            if opcao == '0':
                print('Fechando o programa! ')
                break
            else:
                try:
                    num1 = float(input('Digite o primeiro número:\n'))
                    operacao = input('Digite a operação (+, -, *, /):\n')
                    num2 = float(input('Digite o segundo número:\n'))
                    if operacao == '*':
                        resultado = Calculadora.multiplicar(num1, num2)
                        print(f'Resultado: {resultado}')
                    elif operacao == '/':
                        if num2 == 0:
                            print('ERRO! Números não podem ser divididos por 0!')
                        else:
                            resultado = Calculadora.dividir(num1, num2)
                            print(f'Resultado: {resultado}')
                    elif operacao == '+':
                        resultado = Calculadora.somar(num1, num2)
                        print(f'Resultado: {resultado}')
                    elif operacao == '-':
                        resultado = Calculadora.subtrair(num1, num2)
                        print(f'Resultado: {resultado}')
                    else:
                        raise ValueError('ERRO! Digite +, -, / ou * para as operações!')
                except ValueError:
                    print('Insira valores reais ou inteiros para os números')

import os

def calculadora(num1, num2, op):
    if   op == 1:
        return num1 + num2
    elif op == 2:
        return num1 - num2
    elif op == 3:
        return num1 * num2
    else :
        return num1 / num2

def pegarValores(op):
    if (op < 1 or op > 4):
        return
    else:
        num1 = float(input('informe o primeiro numero: '))
        num2 = float(input('informe o segundo numero: '))
        resultado = calculadora(num1, num2, op)
        print('o resultado da operação foi', resultado)
        input()

op = 1

while op != 0:
    print(":Calculadora da Softex:")
    print("Selecione a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Mutiplicação")
    print("4 - Divisão")
    print("0 - Sair \n")

    op = int(input())

    pegarValores(op)

    os.system('cls')

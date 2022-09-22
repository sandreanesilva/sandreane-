def calculadora(num1, num2, op):
    if   op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2
    else:
        return 0

print(":Calculadora da Softex:")
num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))
op = input("Digite a operação desejada (Soma:+, Subtrair:-, Multiplar:*, Dividir:/)")
print('\n', calculadora(num1, num2, op))

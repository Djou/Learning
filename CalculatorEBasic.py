print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

def soma(number1, number2):
    return number1 + number2

def subtracao(number1, number2):
    return number1 - number2

def multiplicacao(number1, number2):
    return number1 * number2

def divisao(number1, number2):
    return number1 * number2

vOper = int(input("Digite sua opção ('1/2/3/4)"))

vNum1 = float(input("Digite o primeiro número"))

vNum2 = float(input("Digite o segundo número"))

if (vOper == 1):
    print(soma(vNum1, vNum2))
elif (vOper == 2):
    print(subtracao(vNum1, vNum2))
elif (vOper == 3):
    print(multiplicacao(vNum1, vNum2))
elif (vOper == 4):
    print(divisao(vNum1, vNum2))


print(vOper)
print(vNum1)
print(vNum2)



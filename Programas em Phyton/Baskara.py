import math

a = float(input ("Digite o valor de A: "))
b = float(input ("Digite o valor de B: "))
c = float(input ("Digite o valor de C: "))

delta = b** 2 - 4  * a * c

if delta == 0:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    print("A unica raiz é: ", raiz1)

else:
    if delta<0:
        print("Não possui raizes reais")
    else:   
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print("A primeira raiz é: ", raiz1)
        print("A segunda raiz é: ", raiz2)


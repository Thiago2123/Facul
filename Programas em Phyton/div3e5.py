numero = float(input("Digite um numero: "))

div1 = numero // 5
resto1 = numero % 5

div2 = numero // 3
resto2 = numero % 3

if resto1 == 0 and resto2 == 0:
    print("FizzBuzz")
else:     
    print(numero)



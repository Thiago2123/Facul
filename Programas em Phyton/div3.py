numero = float(input("Digite um número para ver se é divisivel por 3: "))

div = numero // 3
resto = numero % 3

if resto == 0:
    print("Fizz")
else:
    print(numero)

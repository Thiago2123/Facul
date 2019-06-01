meucartao = int(input("Digite o numero do cartao:"))

cartaolido = 1
encontreicartao = False

while cartaolido !=0 and not encontreicartao:
    cartaolido = int(input("Digite o numero do prox cartao: "))
    if cartaolido == meucartao:
        encontreicartao = True


if encontreicartao:
    print("O cartao esta lá!")
else:
    print("O cartao n esta lá")

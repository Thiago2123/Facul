
decr = True
anterior = int(input("Digite o primeiro numero da sequencia "))

valor = 1

while valor != 0 and decr:             
    valor = int(input("Digite o prox numero da sequencia "))
    if valor > anterior:
        decr = False
    anterior = valor

if decr:
    print("A sequencia esta decrescente")
else:
    print("a sequencia n esta" )

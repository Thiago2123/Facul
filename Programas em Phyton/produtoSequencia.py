tamanho = int(input("Digite a quantidade de numeros a ser multiplicado: "))

produto = 1
n = 0

while n < tamanho:
    valor= int(input ("Digite um valor: "))
    produto = produto * valor
    n = n + 1
print ("a multiplicaçao é:" , produto)

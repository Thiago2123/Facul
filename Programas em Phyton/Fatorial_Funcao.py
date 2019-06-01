def fatorial(n):
    fat = 1

    while(n > 1):
        fat = fat * n
        n = n - 1
    return fat


def numero_biominal(n, k):
    return fatorial(n) // (fatorial(k) * fatorial(n-k))



def teste_fatorial():
    if fatorial(1) == 1:
        print("funciona pro 1")
    else:
        print("nao funciona pro 1")
    if fatorial(2) == 2:
        print("funciona pro 2")
    else:
        print("nao funciona pro 2")
    if fatorial(0) == 1:
        print("funciona pro 0")
    else:
        print("nao funciona pro 0")
    if fatorial(5) == 120:
        print("funciona pro 5")
    else:
        print("nao funciona pro 5")

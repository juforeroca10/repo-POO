print("Bienvenido, este programa sirve para conocer si la palabra que ingresas es un palindromo.")
def es_palindromo(palabra):
    i: int = 0
    j: int = len(palabra) - 1
    palindromo: bool = True

    while i < j:
        if palabra[i] != palabra[j]:
            palindromo = False
            break
        i += 1
        j -= 1

    return palindromo
palabra = input("Ingresa una palabra: ")
if es_palindromo(palabra):
    print("Si es un palindromo.")
else:
    print("No es un palindromo.")

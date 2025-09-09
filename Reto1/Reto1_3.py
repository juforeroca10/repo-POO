print("Bienvenido, este programa sirve para conocer si el numero que ingresas es un numero primo.")
numeros: str 
numeros_texto: list[str] = []
lista_numeros: list[float] = []
primos: list[int] = []

def es_primo(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filtrar_primos(lista: list[int]) -> list[int]:
    resultado: list[int] = []
    for numero in lista:
        if es_primo(numero):
            resultado.append(numero)
    return resultado

numeros = input("Ingresa numeros separados por comas (1,2,3,4): ")
numeros_texto = numeros.split(",")
lista_numeros = [int(x.strip()) for x in numeros_texto]

primos = filtrar_primos(lista_numeros)

print("Los numeros primos son:", primos)

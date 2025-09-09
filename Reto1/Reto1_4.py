print("Bienvenido, este programa sirve para hallar la mayor suma entre dos elementos consecutivos")
numeros: str 
numeros_texto: list[str] = []
lista_numeros: list[int] = []
mayor_suma: int = 0

def mayor_suma_consecutiva(lista: list[int]) -> int:
    max_suma: int = lista[0] + lista[1]
    for i in range(1, len(lista) - 1):
        suma_actual: int = lista[i] + lista[i + 1]
        if suma_actual > max_suma:
            max_suma = suma_actual
    return max_suma

numeros = input("Ingresa numeros enteros separados por comas (1,2,3,4,): ")
numeros_texto = numeros.split(",")
lista_numeros = [int(x.strip()) for x in numeros_texto]

mayor_suma = mayor_suma_consecutiva(lista_numeros)

print("La mayor suma entre dos elementos consecutivos es:", mayor_suma)

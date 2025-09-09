print("Bienvenido, este programa te ayuda a conocer palabras anagramas.")
palabras: str
palabras_texto: list[str] = []
lista_palabras: list[str] = []
resultado: list[str] = []

def filtrar_anagramas(lista: list[str]) -> list[str]:
    agrupadas: dict[str, list[str]] = {}
    for palabra in lista:
        clave: str = "".join(sorted(palabra))
        if clave in agrupadas:
            agrupadas[clave].append(palabra)
        else:
            agrupadas[clave] = [palabra]

    resultado: list[str] = []
    for grupo in agrupadas.values():
        if len(grupo) > 1:
            resultado.extend(grupo)
    return resultado

palabras = input("Ingresa palabras pero separalas por comas: ")
palabras_texto = palabras.split(",")
lista_palabras = [x.strip() for x in palabras_texto]

resultado = filtrar_anagramas(lista_palabras)

print("Las palabras con los mismos caracteres:", resultado)

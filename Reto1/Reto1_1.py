print("Bienvenido, este programa te ayuda a hacer operaciones basicas.")
def operar(num_1, num_2, operador):
    if operador == "+":
        return num_1 + num_2
    elif operador == "-":
        return num_1 - num_2
    elif operador == "*":
        return num_1 * num_2
    elif operador == "/":
        if num_2 != 0:
            return num_1 / num_2
        else:
            return "No se puede dividir por 0."
    else:
        return "El operador que escribiste no es valido."
num_1 = float(input("Ingresa el primer numero (puede tener decimales): "))
num_2 = float(input("Ingresa el segundo numero (puede tener decimales): "))
operador = input("Ingresa el operador basico que quieras (+, -, *, /): ")
resultado = operar(num_1, num_2, operador)
print(resultado)

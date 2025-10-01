# Introducción
Este es mi primer repositorio, y lo estoy utilizando para aprender a documentar, organizar y compartir mi trabajo de forma profesional. Reúne los ejercicios y retos que he desarrollado durante mis clases de Programación Orientada a Objetos (POO) con el profesor Felipe y seguiré actualizándolo con nuevos retos a medida que avance en mi aprendizaje.
# Reto 1
En el reto 1 nos piden desarrollar una serie de ejercicios prácticos en Python, cada uno como un programa independiente. Los ejercicios incluyen operaciones matemáticas básicas entre dos números, verificación de palíndromos sin usar slicing, filtrado de números primos desde una lista, cálculo de la mayor suma entre elementos consecutivos, y detección de palabras que comparten los mismos caracteres. La idea es aplicar funciones, condicionales y lógica básica para resolver cada problema.
## 1.1
Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: `(1,2,"+")`, salida `(3)`.
### Codigo
```python
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


```
[Función que realiza operaciones básicas](Reto1/Reto1_1.py)
### ¿Cómo llegué al resultado
En este punto nos piden que realicemos una función donde el usuario introduzca sus propios datos, es decir, `num_1`, `num__2` y `operador`; para esto lo primero que hice fue definir la función `def operar` con sus 3 variables y para que se cumpla alguna de las tres operaciones hacer unas condicionales `if`, `elif` y `else`, que sirven para comparar y ver que operación se quiere realizar, y si se escribe un caracter diferente a los pedidos se da el error de que no ingreso uno válido. Después de esto, coloque un `input` para obtener los tres datos y un `print` para que muestre la operación al final.
## 1.2
Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.
### Codigo
```python
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
```
[Función que valida si es un palíndromo](Reto1/Reto1_2.py)
### ¿Cómo llegué al resultado?
En este punto nos piden hacer una función que permita revisar si la palabra que introduzca el usuario es un palíndromo o no, para empezar ni siquiera sabia que era slicing así que no me parecio algo del otro mundo no usarlo, empece definiendo la función `def es_palindromo`, dentro de esta función hay una variable en `str` llamada `palabra`, también dos `int` que nos ayudarán luego para el ciclo que use, y por último una variable en `bool` que esta en `True`, luego de esto dos variables en `int` y una función llamada `len` que permite ver cuántos elementos hay en una secuencia. Luego de esto el ciclo `while` acompañado por un `if` nos permite recorrer el string por cada una de sus letras para asi corroborar si son iguales o no. Si son iguales la variable en `bool` sigue en `True` y nos muestra que la palabra que ingreso el usuario si es un palíndromo, y si el ciclo detecta que la palabra no es igual en alguna letra pues la variable `palabra` se convierte en `False` y nos saca del ciclo para dar el mensaje de que no es palíndromo. (Si se escribe la primera letra en mayuscula no lo toma como palíndromo).
## 1.3
Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.
### Codigo
```python
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
```
[Función que filtra los números primos](Reto1/Reto1_3.py)
### ¿Cómo llegué al resultado?
En este punto nos piden hacer una función que permita filtrar que números son primos y mostrarlos, por ende, comienzo pidiendo al usuario que ingrese varios números separados por comas. Esa entrada se guarda en la variable `numeros` que es un `str`. Luego, esa cadena se divide usando `.split(",")`, lo que genera la primera lista llamada `numeros_texto`, esta lista tiene los números aún como texto. Después, creo la segunda lista llamada `lista_numeros`, que convierte cada elemento de `numeros_texto` en un número entero. Para eso se usa la expresión `[int(x.strip()) for x in numeros_texto]`, que también se usa para eliminar los espacios innecesarios. Con esa lista de números, se define la función `def filtrar_primos`, que recorre `lista_numeros` y verifica cuáles son primos usando la función `es_primo`. Los números que cumplen esa condición se agregan a la tercera lista, llamada `primos`. Y al final, se muestra el contenido de `primos`, que serian los números ingresados por el usuario al principio ya filtrados.
## 1.4
Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.
### Codigo
```python
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
```
[Función que realiza la mayor suma](Reto1/Reto1_4.py)
### ¿Cómo llegué al resultado?
En este punto nos piden hacer una función que permita encontrar la mayor suma entre dos números consecutivos en una lista. Para eso, empece por pedirle al usuario los datos, y luego use `split(",")` para separar los números que venían como texto. Después aplique `strip()` para limpiar espacios y `int()` para convertir cada número en entero. Ya con la lista, cree una función que recorre los elementos con un `for`, sumando cada número con el siguiente usando `lista[i] + lista[i + 1]`. Para guardar la mejor suma, use una variable llamada `max_suma` y se actualiza si encontra una suma mayor. Al final, se muestra el valor que se calcule de todo este proceso.
## 1.5
Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres. e.g. entrada: `["amor", "roma", "perro"]`, salida `["amor", "roma"]`
### Codigo
```python
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
```
[Función que muestra los anagramas](Reto1/Reto1_5.py)
### ¿Cómo llegué al resultado?
En este punto se quería hacer un programa que detectara palabras que son anagramas entre sí, es decir, que tienen los mismos caracteres pero en distinto orden. Primero pedí al usuario que ingresara varias palabras separadas por comas. Como esa entrada viene como texto, la separé con `.split(",")` y luego usé `strip()` para limpiar espacios. Ya con la lista de palabras lista, creé una función que agrupa las palabras según sus letras ordenadas. Para eso, tomé cada palabra, la convertí en una lista de letras, la ordené con `sorted()` y la volví a unir con `"".join()`. Esa cadena ordenada la usé como clave en un diccionario, y fui guardando ahí todas las palabras que compartían esa misma clave. Al final, revisé ese diccionario y extraje solo los grupos que tenían más de una palabra, porque eso significa que son anagramas.
# Reto 2
Elija un problema de la vida real (sistema de gestión de biblioteca, negocio de compra-venta, automóvil, etc) que se pueda modelar a través de objetos y clases. Plantee las relaciones de clases, composiciones, propiedades y comportamientos del sistema en uno mas diagramas tipo UML.
### Solución
![Diagrama UML sobre un sistema de reservas de vuelo](Reto_2.drawio.png)
 **Descripción**
- Las flechas vacias, significan que Empleado y Pasajero son una herencia de Persona y Vuelo es herencia de Avión.
- Los rombos, significan que a los que estan apuntando es una composición.
# Reto 3
**Restaurant scenario:** You want to design a program to calculate the bill for a customer's order in a restaurant.
- Define a base class *MenuItem*: This class should have attributes like name, price, and a method to calculate the total price.
- Create subclasses for different types of menu items: Inherit from *MenuItem* and define properties specific to each type (e.g., Beverage, Appetizer, MainCourse). 
- Define an Order class: This class should have a list of *MenuItem* objects and methods to add items, calculate the total bill amount, and potentially apply specific discounts based on the order composition.

Create a class diagram with all classes and their relationships. 
The menu should have at least 10 items.
The code should follow PEP8 rules.
## Solución
### Código
- Clase *MenuItem* y sus diferentes subclases.

  
```python
class MenuItem:
    def __init__(self, name: str, price: float, description: float) -> None:
        self.name = name
        self.price = price
        self.description = description

    def get_total_price(self) -> float:
        return self.price

    def show_info(self) -> str:
        return f"{self.name}: ${self.price:.2f} - {self.description}"

    def update_price(self, new_price: float) -> None:
        self.price = new_price


class MainCourse(MenuItem):
    def __init__(self, name: str, price: float, description: float,
                 vegetarian: bool, side_dish: str, spice_level: str) -> None:
        super().__init__(name, price, description)
        self.vegetarian = vegetarian
        self.side_dish = side_dish
        self.spice_level = spice_level

    def is_spicy(self) -> bool:
        return self.spice_level.lower() in ["medium", "high"]

    def add_side_dish(self, new: str) -> None:
        self.side_dish = new

    def change_vegetarian(self, value: bool) -> None:
        self.vegetarian = value


class Dessert(MenuItem):
    def __init__(self, name: str, price: float, description: float,
                 sugar_free: bool, gluten_free: bool, type: str) -> None:
        super().__init__(name, price, description)
        self.sugar_free = sugar_free
        self.gluten_free = gluten_free
        self.type = type

    def is_diabetic_friendly(self) -> bool:
        return self.sugar_free

    def change_type(self, new_type: str) -> None:
        self.type = new_type

    def show_restrictions(self) -> str:
        restrictions = []
        if self.sugar_free:
            restrictions.append("sugar-free")
        if self.gluten_free:
            restrictions.append("gluten-free")
        return ", ".join(restrictions)


class Drink(MenuItem):
    def __init__(self, name: str, price: float, description: float,
                 size: str, ice: bool, alcoholic: bool, fizzy: bool) -> None:
        super().__init__(name, price, description)
        self.size = size
        self.ice = ice
        self.alcoholic = alcoholic
        self.fizzy = fizzy

    def is_large(self) -> bool:
        return self.size.lower() == "large"

    def add_ice(self) -> None:
        self.ice = True

    def change_size(self, new_size: str) -> None:
        self.size = new_size


class Appetizer(MenuItem):
    def __init__(self, name: str, price: float, description: float,
                 temperature: str, portions: int, large: bool) -> None:
        super().__init__(name, price, description)
        self.temperature = temperature
        self.portions = portions
        self.large = large

    def is_hot(self) -> bool:
        return self.temperature.lower() == "hot"

    def split_portions(self, quantity: int) -> None:
        self.portions = quantity

    def change_temperature(self, new_temp: str) -> None:
        self.temperature = new_temp


class Soup(MenuItem):
    def __init__(self, name: str, price: float, description: float,
                 soup_type: str, size: str, vegetarian: bool) -> None:
        super().__init__(name, price, description)
        self.soup_type = soup_type
        self.size = size
        self.vegetarian = vegetarian

    def is_hot(self) -> bool:
        return True  # Assuming all soups are served hot

    def change_size(self, new_size: str) -> None:
        self.size = new_size

    def side_suggestion(self) -> str:
        return "Artisan bread"


class Combo(MenuItem):
    def __init__(self, name: str, price: float, description: float,
                 included_items: list[str], includes_drink: bool, combo_price: float) -> None:
        super().__init__(name, price, description)
        self.included_items = included_items
        self.includes_drink = includes_drink
        self.combo_price = combo_price

    def add_item(self, new_item: str) -> None:
        self.included_items.append(new_item)

    def includes_dessert(self) -> bool:
        return any("dessert" in item.lower() for item in self.included_items)

    def show_items(self) -> str:
        return ", ".join(self.included_items)


```
- Clase *Order* y un ejemplo de uso con menú ya definido y pedido de 3 productos.

  
```python
class Order:
    def __init__(self, date: str, status: str) -> None:
        self.items: list[MenuItem] = []
        self.date = date
        self.status = status

    def add_item(self, item: MenuItem) -> None:
        self.items.append(item)

    def calculate_total(self) -> float:
        subtotal = sum(item.get_total_price() for item in self.items)
        if len(self.items) >= 3:
            discount = subtotal * 0.10
            return subtotal - discount
        return subtotal

    def show_summary(self) -> None:
        print(f"\n--- ORDER SUMMARY ---")
        print(f"Date: {self.date}")
        print(f"Status: {self.status}")
        print("Items:")
        for item in self.items:
            print(f"- {item.show_info()}")
        print(f"Total: ${self.calculate_total():,.2f} COP")



# Drinks
drink1 = Drink("Mango Juice", 8500.0, 1.0, "medium", True, False, False)
drink2 = Drink("Craft Beer", 14500.0, 1.0, "large", False, True, False)
drink3 = Drink("Sparkling Water", 6500.0, 1.0, "small", False, False, True)

# Main Courses
main1 = MainCourse("Bandeja Paisa", 28000.0, 1.0, False, "rice and beans", "medium")
main2 = MainCourse("Mediterranean Salad", 22000.0, 1.0, True, "whole grain bread", "mild")
main3 = MainCourse("Grilled Chicken", 25000.0, 1.0, False, "mashed potatoes", "high")

# Desserts
dessert1 = Dessert("Chocolate Cake", 12000.0, 1.0, False, False, "cake")
dessert2 = Dessert("Fresh Fruit", 9500.0, 1.0, True, True, "fruit")
dessert3 = Dessert("Vanilla Ice Cream", 11000.0, 1.0, False, False, "ice cream")

# Appetizers
appetizer1 = Appetizer("Mini Arepas with Cheese", 10500.0, 1.0, "hot", 4, True)
appetizer2 = Appetizer("Guacamole with Chips", 9800.0, 1.0, "cold", 2, False)
appetizer3 = Appetizer("Stuffed Mushrooms", 11500.0, 1.0, "hot", 6, True)

# Soups
soup1 = Soup("Ajiaco Santafereño", 18000.0, 1.0, "ajiaco", "large", False)
soup2 = Soup("Cream of Mushrooms", 16500.0, 1.0, "cream", "medium", True)
soup3 = Soup("Vegetable Broth", 15000.0, 1.0, "broth", "small", True)

# Combos
combo1 = Combo("Executive Combo", 35000.0, 1.0,
               ["Main Course: Bandeja Paisa", "Drink: Mango Juice", "Dessert: Fresh Fruit"],
               True, 33000.0)

combo2 = Combo("Vegetarian Combo", 32000.0, 1.0,
               ["Main Course: Mediterranean Salad", "Soup: Cream of Mushrooms", "Dessert: Fresh Fruit"],
               True, 31000.0)

combo3 = Combo("Family Combo", 58000.0, 1.0,
               ["Appetizer: Stuffed Mushrooms", "Main Course: Grilled Chicken", "Drink: Sparkling Water", "Dessert: Vanilla Ice Cream"],
               True, 55000.0)

# Display menu
print("--- AVAILABLE MENU ---\n")

for item in [drink1, drink2, drink3,
             main1, main2, main3,
             dessert1, dessert2, dessert3,
             appetizer1, appetizer2, appetizer3,
             soup1, soup2, soup3,
             combo1, combo2, combo3]:
    print(item.show_info())

# Create an order
order1 = Order("2025-10-01", "Pending")

# Add items from your menu
order1.add_item(main1)
order1.add_item(drink1)
order1.add_item(dessert2)

# Show summary
order1.show_summary()
```
[Código Completo sobre el Restaurante](Reto3.py)
### UML
![Diagrama UML sobre un sistema de restaurante](UML_Reto_3.drawio.png)

import math

class MenuItem:
    def __init__(self, name: str, price: float, description: float) -> None:
        self._name = name
        self._price = price
        self._description = description

    def get_name(self) -> str:
        return self._name

    def set_name(self, new_name: str) -> None:
        self._name = new_name

    def get_price(self) -> float:
        return self._price

    def set_price(self, new_price: float) -> None:
        if new_price >= 0:
            self._price = new_price

    def get_description(self) -> float:
        return self._description

    def set_description(self, new_description: float) -> None:
        self._description = new_description

    def get_total_price(self) -> float:
        return self._price

    def show_info(self) -> str:
        return f"{self._name}: ${self._price:.2f} - {self._description}"


class MainCourse(MenuItem):
    def __init__(self, name, price, description, vegetarian, side_dish, spice_level):
        super().__init__(name, price, description)
        self._vegetarian = vegetarian
        self._side_dish = side_dish
        self._spice_level = spice_level

    def is_spicy(self):
        return self._spice_level.lower() in ["medium", "high"]

    def get_vegetarian(self):
        return self._vegetarian

    def set_vegetarian(self, value):
        self._vegetarian = value

    def get_side_dish(self):
        return self._side_dish

    def set_side_dish(self, new):
        self._side_dish = new

    def get_spice_level(self):
        return self._spice_level

    def set_spice_level(self, level):
        self._spice_level = level


class Dessert(MenuItem):
    def __init__(self, name, price, description, sugar_free, gluten_free, type):
        super().__init__(name, price, description)
        self._sugar_free = sugar_free
        self._gluten_free = gluten_free
        self._type = type

    def is_diabetic_friendly(self):
        return self._sugar_free

    def get_type(self):
        return self._type

    def set_type(self, new_type):
        self._type = new_type

    def get_sugar_free(self):
        return self._sugar_free

    def set_sugar_free(self, value):
        self._sugar_free = value

    def get_gluten_free(self):
        return self._gluten_free

    def set_gluten_free(self, value):
        self._gluten_free = value

    def show_restrictions(self):
        restrictions = []
        if self._sugar_free:
            restrictions.append("sugar-free")
        if self._gluten_free:
            restrictions.append("gluten-free")
        return ", ".join(restrictions)


class Drink(MenuItem):
    def __init__(self, name, price, description, size, ice, alcoholic, fizzy):
        super().__init__(name, price, description)
        self._size = size
        self._ice = ice
        self._alcoholic = alcoholic
        self._fizzy = fizzy

    def is_large(self):
        return self._size.lower() == "large"

    def get_size(self):
        return self._size

    def set_size(self, new_size):
        self._size = new_size

    def get_ice(self):
        return self._ice

    def set_ice(self, value):
        self._ice = value

    def get_alcoholic(self):
        return self._alcoholic

    def set_alcoholic(self, value):
        self._alcoholic = value

    def get_fizzy(self):
        return self._fizzy

    def set_fizzy(self, value):
        self._fizzy = value


class Appetizer(MenuItem):
    def __init__(self, name, price, description, temperature, portions, large):
        super().__init__(name, price, description)
        self._temperature = temperature
        self._portions = portions
        self._large = large

    def is_hot(self):
        return self._temperature.lower() == "hot"

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, new_temp):
        self._temperature = new_temp

    def get_portions(self):
        return self._portions

    def set_portions(self, quantity):
        self._portions = quantity

    def get_large(self):
        return self._large

    def set_large(self, value):
        self._large = value


class Soup(MenuItem):
    def __init__(self, name, price, description, soup_type, size, vegetarian):
        super().__init__(name, price, description)
        self._soup_type = soup_type
        self._size = size
        self._vegetarian = vegetarian

    def is_hot(self):
        return True

    def get_size(self):
        return self._size

    def set_size(self, new_size):
        self._size = new_size

    def get_soup_type(self):
        return self._soup_type

    def set_soup_type(self, new_type):
        self._soup_type = new_type

    def get_vegetarian(self):
        return self._vegetarian

    def set_vegetarian(self, value):
        self._vegetarian = value

    def side_suggestion(self):
        return "Artisan bread"


class Combo(MenuItem):
    def __init__(self, name, price, description, included_items, includes_drink, combo_price):
        super().__init__(name, price, description)
        self._included_items = included_items
        self._includes_drink = includes_drink
        self._combo_price = combo_price

    def add_item(self, new_item):
        self._included_items.append(new_item)

    def includes_dessert(self):
        return any("dessert" in item.lower() for item in self._included_items)

    def show_items(self):
        return ", ".join(self._included_items)

    def get_combo_price(self):
        return self._combo_price

    def set_combo_price(self, new_price):
        self._combo_price = new_price


class Order:
    def __init__(self, date, status):
        self.items = []
        self.date = date
        self.status = status

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        has_main = any(isinstance(item, MainCourse) for item in self.items)
        total = 0.0
        for item in self.items:
            price = item.get_total_price()
            if has_main and isinstance(item, Drink):
                price *= 0.9  # 10% discount
            total += price
        return total

    def show_summary(self):
        print(f"\n--- ORDER SUMMARY ---")
        print(f"Date: {self.date}")
        print(f"Status: {self.status}")
        print("Items:")
        for item in self.items:
            print(f"- {item.show_info()}")
        print(f"Total: ${self.calculate_total():,.2f} COP")


class Payment:
    def __init__(self, amount, method):
        self.amount = amount
        self.method = method
        self.status = "Pending"

    def process_payment(self):
        self.status = "Completed"

    def show_receipt(self):
        print("\n--- PAYMENT RECEIPT ---")
        print(f"Amount: ${self.amount:,.2f} COP")
        print(f"Method: {self.method}")
        print(f"Status: {self.status}")
# Create an order
order1 = Order("2025-10-10", "Pending")

# Add items from your menu
order1.add_item(MainCourse("Bandeja Paisa", 28000.0, 1.0, False, "rice and beans", "medium"))
order1.add_item(Drink("Craft Beer", 14500.0, 1.0, "large", False, True, False))
order1.add_item(Dessert("Vanilla Ice Cream", 11000.0, 1.0, False, False, "ice cream"))

# Show order summary
order1.show_summary()

# Process payment
total_amount = order1.calculate_total()
payment1 = Payment(total_amount, "Credit Card")
payment1.process_payment()
payment1.show_receipt()

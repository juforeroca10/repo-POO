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

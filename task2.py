class Store:
    def __init__(self, name, address, items=None):
        self.name = name
        self.address = address
        self.items = items if items is not None else {}

    def add_item(self, item_name, price):
        if price <= 0:
            raise ValueError("Цена должна быть положительной")
        if item_name in self.items:
            print(f"Внимание: товар '{item_name}' уже есть, обновляем цену")
        self.items[item_name] = price

    def del_atems(self, item_name):
        self.items.pop(item_name, None)

    def get_price(self, item_name):
        if item_name in self.items:
            return self.items[item_name]
        return None

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            return True
        return False

my_store1 = Store('Перекресток', "ул. Мира,1", None)
my_store1.add_item("Молоко", 85.50)
my_store1.add_item("Хлеб", 45.30)


my_store2 = Store('Дикси', "ул. Ленина,5", None)
my_store2.add_item("Сметана", 130.50)
my_store2.add_item("Хлеб", 55.60)
my_store2.add_item("Яблоки", 225.00)

my_store3 = Store('Пятёрочка', "ул. Победы,10", None)
my_store3.add_item("Чай", 250.00)
my_store3.add_item("Сало", 90.10)
my_store3.add_item("Помидоры", 315.00)

# Добавляем товар
print(my_store1.get_price("Яйца"))
my_store1.add_item("Яйца", 120.00)
print(my_store1.get_price("Яйца"))

# Получаем цену
print(my_store1.get_price("Хлеб"))

# Обновляем цену
my_store1.update_price("Молоко", 90.00)
print(my_store1.get_price("Молоко"))

# Удаляем товар
my_store1.del_atems("Яйца")
print(my_store1.get_price("Яйца"))

# Выводим информацию о магазине




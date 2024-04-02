class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    # Метод для добавления товара в ассортимент
    def add_item(self, item_name, price):
        self.items[item_name] = price

    # Метод для удаления товара из ассортимента
    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    # Метод для получения цены товара по его названию
    def get_price(self, item_name):
        return self.items.get(item_name, None)

    # Метод для обновления цены товара
    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

    def get_assortment(self):
        if len(self.items) == 0:
            print("Товары не добавлены")
            return
        print(f"\nАссортимент магазина {self.name} по адресу {self.address}:")
        for item_name, price in self.items.items():
            print(f"{item_name.ljust(16)[:16]} Цена: {price}")
        print()


store1 = Store("Ашан", "Абрикосовая, 16")
store2 = Store("Евроспар", "Виноградная, 32")
store3 = Store("Авокадо", "Яблочная, 64")

# Добавление товаров в магазины
store1.add_item("Apples", 99.50)
store1.add_item("Bananas", 89.50)

store2.add_item("Chocolate", 89.90)
store2.add_item("Ferrero Rocher", 899.90)
store2.add_item("Nescafe", 199.50)
store2.add_item("Сасао", 149.50)

store3.add_item("Milk", 79.50)
store3.add_item("Yogurt", 69.50)

print("Проверяем работу методов на примере магазина 'Евроспар':")

# Добавление товара
store2.add_item("Marshmallows", 149.90)
print(f"\nПосле добавления пастилы:")
store2.get_assortment()

# Обновление цены товара
store2.update_price("Nescafe", 299.50)
print(f"Обновленная цена Nescafe: {store2.get_price('Nescafe')}")

# Удаление товара
store2.remove_item("Сасао")
print(f"\nПосле удаления какао:")
store2.get_assortment()

# Получение цены товара
print(f"Цена конфет 'Ferrero Rocher': {store2.get_price('Ferrero Rocher')}")
print()
print(f"Попробуем получить цену удаленного товара (какао): {store2.get_price('Сасао')}")

class Shoe:
    def init(self, brand, size, color, price):
        self.brand = brand
        self.size = size
        self.color = color
        self.price = price

    def display_info(self):
        return f"Обувь: {self.brand} (Размер: {self.size}, Цвет: {self.color}, Цена: {self.price} руб.)"

sneakers = Shoe(brand="Nike", size=42, color="синий", price=4500)
print(sneakers.display_info())

boots = Shoe(brand="Timberland", size=44, color="коричневый", price=12000)
print(boots.display_info())
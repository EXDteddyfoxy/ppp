class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Hero(Person):
    def __init__(self, name, age, superpower):
        super().__init__(name, age)
        self.superpower = superpower


hero = Hero("Superman", 30, "Flying")
print(hero.name, hero.age, hero.superpower)
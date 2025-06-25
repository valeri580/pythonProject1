#1. Создайте базовый класс `Animal`, который будет содержать
# общие атрибуты (например, `name`, `age`) и методы (`make_sound()`,
# `eat()`) для всех животных.

#2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и
# `Reptile`, которые наследуют от класса `Animal`. Добавьте
# специфические атрибуты и переопределите методы, если требуется
# (например, различный звук для `make_sound()`).

#3. Продемонстрируйте полиморфизм: создайте функцию
# `animal_sound(animals)`, которая принимает список животных
# и вызывает метод `make_sound()` для каждого животного.

#4. Используйте композицию для создания класса `Zoo`,
# который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.

#5. Создайте классы для сотрудников, например, `ZooKeeper`,
# `Veterinarian`, которые могут иметь специфические методы (например,
# `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

class Zoo():
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Сотрудник {employee.name} принят на работу")

    def show_animals(self):
        print("\nЖивотные в зоопарке:")
        for animal in self.animals:
            print(animal)

    def show_employees(self):
        print("\nСотрудники зоопарка:")
        for employee in self.employees:
            print(employee)

class Employee():
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return f"{self.name} (ID: {self.id})"

class ZooKeeper(Employee):
    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}. {animal.name} ест {animal.eat()}")

class Veterinarian(Employee):
    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")


class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def make_sound(self):
        return "..."

    def eat(self):
        return "..."

    def __str__(self):
        if self.age % 10 == 1 and self.age % 100 != 11:
            age_word = "год"
        elif 2 <= self.age % 10 <= 4 and (self.age % 100 < 10 or self.age % 100 >= 20):
            age_word = "года"
        else:
            age_word = "лет"
        return f"{self.name} ({self.age} {age_word})"

class Bird(Animal):
    def make_sound(self):
        return "чирик"

    def eat(self):
        return "зерно"

class Mammal(Animal):
    def make_sound(self):
        return "мяу"

    def eat(self):
        return "мясо"

class Reptile(Animal):
    def make_sound(self):
        return "шипение"

    def eat(self):
        return "капусту"

def animal_sound(animals):
    for animal in animals:
        print(f"{animal.name} издаёт звук: {animal.make_sound()}")


animals = [
    Bird("Воробей", 2),
    Mammal("Кот", 3),
    Reptile("Черепаха", 10)
]

animal_sound(animals)

my_zoo = Zoo("Вместе")

my_zoo.add_animal(Bird("Попугай", 5))
my_zoo.add_animal(Mammal("Лев", 7))
my_zoo.add_animal(Reptile("Игуана", 4))

keeper = ZooKeeper("Иван Петров", 1 )
vet = Veterinarian("Анна Сидорова", 2)

my_zoo.add_employee(keeper)
my_zoo.add_employee(vet)

keeper.feed_animal(my_zoo.animals[0])
vet.heal_animal(my_zoo.animals[1])

my_zoo.show_animals()
my_zoo.show_employees()

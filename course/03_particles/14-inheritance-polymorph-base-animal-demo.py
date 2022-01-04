# Если у нас большая иерархия: https://natureofcode.com/book/imgs/chapter04/ch04_02.png
# Замучаемся создавать все эти специфичные классы
# Вводим базовый

class Animal:
    # Dog и Cat будут наследовать аттрибут класса age.
    def __init__(self, age):
        super().__init__(age)

    # Dog и Cat наследуют функции eat() и sleep().
    def eat(self):
        print("Yum!")

    def sleep(self):
        self.age += 1 / 365
        print("Zzzzzz")

# Dogs и Cats имеют в качестве атрибутов age (возраст) и один набор функций eat, sleep.
class Dog(Animal):
    def __init__(self, age):
        super().__init__(age)

    def bark(self):
        print("WOOF!")


class Cat:
    def __init__(self, age):
        super().__init__(age)

    def meow(self):
        print("MEOW!")

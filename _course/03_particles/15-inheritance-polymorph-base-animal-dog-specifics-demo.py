# У собаки появляется некоторая специфика

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
    def __init__(self, age, color):
        self.haircolor = color
        super().__init__(age)

    # A Dog's specific eating characteristics
    def eat(self):
        print(f"I am {self.haircolor} dog!")
        super().eat()

    def bark(self):
        print("WOOF!")


class Cat:
    def __init__(self, age):
        super().__init__(age)

    def meow(self):
        print("MEOW!")

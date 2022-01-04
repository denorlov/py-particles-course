# Dogs и Cats имеют в качестве атрибутов age (возраст) и один набор функций eat, sleep.
class Dog:
    def __init__(self, age):
        self.age = age

    def eat(self):
        print("Yum!")

    def sleep(self):
        self.age += 1 / 365
        print("Zzzzzz")

    # Лаять умеет только собака
    def bark(self):
        print("WOOF!")


class Cat:
    def __init__(self, age):
        self.age = age

    def eat(self):
        print("Yum!")

    def sleep(self):
        self.age += 1/365
        print("Zzzzzz")

    def meow(self):
        print("MEOW!")

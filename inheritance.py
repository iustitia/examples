

class Animal:

    def __init__(self):
        pass

    def play(self):
        print("playing....")

    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        print("meow")


class Dog(Animal):
    def make_sound(self):
        print("bark")


animals = []
animals.append(Cat())
animals.append(Cat())
animals.append(Dog())


for animal in animals:
    animal.make_sound()

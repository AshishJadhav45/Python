class Animal:
    def make_sound(self):
        pass


class dog(Animal):
    def make_sound(self):
        return "woof"

class cat (Animal):
    def make_sound(self):
        return "Meow"

animals = [dog(), cat()]

for Animal in animals:

# Parent Class (Superclass)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    # This method will be overridden by the child classes
    def make_sound(self):
        pass 

# Child Classes (Subclasses) inheriting from Animal
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Lion(Animal):
    def make_sound(self):
        return "Roar!"

# Creating instances (Objects)
dog = Dog("Rex", "Dog")
cat = Cat("Whiskers", "Cat")
lion = Lion("Simba", "Lion")

# Polymorphism in action: Same interface/method name, different behaviors
animals = [dog, cat, lion]

for animal in animals:
    print(f"The {animal.species} named {animal.name} goes: {animal.make_sound()}")
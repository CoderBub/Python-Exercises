#Polymorphism
class Animal:
    def speak(self):
        pass

    def walk(speak):
        print("I am walking.")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Owl(Animal):
    def speak(self):
        print("Hoot!")

    def walk(self):
        print("I am flying.")

animals = [Dog(), Cat(), Owl()]
for animal in animals:
    animal.walk()
    animal.speak()           # same call, different behavior

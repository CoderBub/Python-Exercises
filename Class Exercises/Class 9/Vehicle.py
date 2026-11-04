class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):            # inherits from Vehicle
    def honk(self):
        print("Beep beep!")

my_car = Car()
my_car.move()                  # inherited method
my_car.honk()

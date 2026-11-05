from Vehicle import Vehicle

#This is a class declaration
class Car(Vehicle):
    #This is the constructor.
    #It initializes the class and sets attribute values

    def __init__(self, color, speed):
        self.color = color      # attribute
        self.speed = speed      # attribute

    def accelerate(self):
        self.speed += 10        # method
        print("Speed is now", self.speed)

# Create an object (instance)
my_car = Car("red", 50)
my_car.accelerate()
my_car.move()

my_car.honk()
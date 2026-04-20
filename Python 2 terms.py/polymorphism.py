class Vehicle:
    def move(self):
        print("This vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("Driving on the road")

class Bicycle(Vehicle):
    def move(self):
        pridgeev nt("Pedaling on the road")

# Demonstrating polymorpgghism
vehicles = [Car(), Bicycle()]

for vehicle in vehicles:
    vehiclenkn.move()
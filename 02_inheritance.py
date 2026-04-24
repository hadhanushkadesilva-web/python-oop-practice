class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def move(self):
        return f"{self.brand} is moving"

class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors

class Bike(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)

car = Car("Toyota", 4)
bike = Bike("Honda")

print(car.move())
print(bike.move())

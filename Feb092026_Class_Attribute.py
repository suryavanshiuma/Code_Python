class Car:

    wheels = 4 # class attribute (shared by all instances)

    def __init__(self, brand, model):
        self.brand=brand
        self.model=model

# creating instances of the car class
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

print(car1.wheels)
print(car2.wheels)

print(car1.brand)
print(car2.brand)
print(car1.model)
print(car2.model)



        

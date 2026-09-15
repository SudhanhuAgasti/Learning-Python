#QN> crate an electriCar class that inherits from the Car class and has an additional attribute.


class Car:  # class name alawyas capital letter
    def __init__(self,brand,model):
        self.brand= brand
        self.model= model

    def full_name(self):
        return f"{self.brand} {self.model}" 


class ElectricCar(Car):
    def __init__(self,brand,model,batterySize):
        super().__init__(brand,model)
        self.batterySize=batterySize



my_car= Car("Toyata","Corola")   
# print("The brand of the car is : ",my_car.brand)
# print("The model of the car is :",my_car.model)
# print("The full name  of the car is :",my_car.full_name())

my_tesla=ElectricCar("Tesla","Model S","85KWH")
# print("the model of the electricCar: ",my_tesla.model)

print("the fullName of the electricCar: ",my_tesla.full_name())
print("the batterySize of the electricCar: ",my_tesla.batterySize)



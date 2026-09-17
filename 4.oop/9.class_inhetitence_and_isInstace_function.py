# QN> Demonstrate the use of instance() to check if my tesla is instance of car and electric car.

class Car: 
    def __init__(self,brand,model):
        self.brand= brand
        self.model= model

    def full_name(self):
        return f"{self.brand} {self.model}" 

    def fuel_type(self):
        return "petrol or Dissel"    


class ElectricCar(Car):
    def __init__(self,brand,model,batterySize):
        super().__init__(brand,model)
        self.batterySize=batterySize

    def fuel_type(self):
        return "Electric charges"      



my_car= Car("Toyata","Corola")   
print("the fuel type of my_car is : ",my_car.fuel_type())


my_tesla=ElectricCar("Tesla","Model S","85KWH")
# print("the fuel type of the electricCar: ",my_tesla.fuel_type())


# isinstance use (ek object dedo, sushremai puch lo kn si class ki hai ?)

print(isinstance(my_tesla,Car))
print(isinstance(my_tesla,ElectricCar))





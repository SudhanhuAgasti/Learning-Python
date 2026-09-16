# QN> Demonostarte ploymorphism by defining a method fuel_type in the both Electric car classes.but with different behaviours.

class Car:  # class name alawyas capital letter
    def __init__(self,brand,model):
        self.brand= brand
        self.model= model

    def full_name(self):
        return f"{self.brand} {self.model}" 


# polymorphism
    def fuel_type(self):
        return "petrol or Dissel"    


class ElectricCar(Car):
    def __init__(self,brand,model,batterySize):
        super().__init__(brand,model)
        self.batterySize=batterySize


# polymorphism
    def fuel_type(self):
        return "Electric charges"      



my_car= Car("Toyata","Corola")   
print("the fuel type of my_car is : ",my_car.fuel_type())


my_tesla=ElectricCar("Tesla","Model S","85KWH")
print("the fuel type of the electricCar: ",my_tesla.fuel_type())




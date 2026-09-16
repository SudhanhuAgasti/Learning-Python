#QN> add a class variable to the Car that keeps track of cars created.

class Car:
    total_car=0
    def __init__(self,brand,model):
        self.brand= brand
        self.model= model

        # kiun ki jitne baar object banega ea __init__  utni baar call hoga .
        Car.total_car +=1

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


#  find the number of  the car.
my_car= Car("Toyata","Corola")  #1
my_car= Car("Tata","Safari")  #2
my_car= Car("Toyata","Fortuner") #3 
my_car= Car("Toyata","Fortuner")  #4



# print("the fuel type of my_car is : ",my_car.fuel_type())

print("The total number of the car is  : ",Car.total_car)







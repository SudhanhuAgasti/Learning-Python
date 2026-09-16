# QN> Modify the car class to encapsulate the brand attribute, making it private and provide a getter.

#  ENCAPSULATION
class Car:
    def __init__(self,brand,model):
        self.__brand= brand
        self.model= model

#  if two underscore write  before the variable it is now private means it can't be access by the object .

# To access this we have to make methods.
    def get_brand(self):
        return self.__brand+ "!(we got the brand)"    




my_car= Car("Toyata","Corola")   
# print("The brand of the car is : ",my_car.__brand)     (we dont have direct access)
print("The modified car class into encapsulate the brand is : ",my_car.get_brand())



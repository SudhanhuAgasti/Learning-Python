# MOVIE TICKET PRICING (12 for adults (18 an over), 8 for children, every one get 2% discount on the wednesday. )

SD_ADULT=int(12-2)
SD_children=int(8-2)
# day="wednes day"
age=int(input("enter ur age:"))
day= input("enter the day :")
# day= day.replace(" ","").lower()

if day=="wednes day":
            if age>=18:
                print("Your ticket price is: $",SD_ADULT)
            else:
                print("Your ticket price is: $",SD_children)    
else:
            if age>18:
                print("Your ticket price is $12")
            else:
                print("Your ticket price is $8")


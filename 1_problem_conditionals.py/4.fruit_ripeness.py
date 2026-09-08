#  fruit ripeness checker!
fruit="Bananna"
fruit_color=input("fill your fruit color(Green/Yellow/Brown): ")

if fruit_color=="Green":
    print(fruit,",It is unripe!");
elif fruit_color=="Yellow":
    print(fruit,",It is Ripe!");
elif fruit_color=="Brown":
    print(fruit,",It is OverRipe!");        
else:
    print("Please provide valid color !")    
# password strength check !

password="239hhhhhhhh7";

if len(password)<6:
    print(password, "The password is weak !");
elif len(password)<10:
    print(password, "The password is Medium!");
elif len(password)>10:
    print(password, "The password is strong !");    

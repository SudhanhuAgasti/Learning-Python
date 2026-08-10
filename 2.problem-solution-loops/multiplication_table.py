#print the multiplicaton table and skip the fifth itreation 

# for(i=1;i<10;i++):
number =int(input("Provide me a number :"))


for i in range(1,11):
    if i==5:
        continue
    print(number,'x',i,'=', number*i)

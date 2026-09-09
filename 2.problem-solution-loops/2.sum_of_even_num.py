# count the summ of even numbers in the list;
# numbers=[1,-2,3,-4,5,6,-7,-8,9,10]

n=10
sum_even=0

for i in range(1,n+1):
    if i%2==0:
        sum_even=sum_even+1
print("The total sum of even is :  ",sum_even)        
    

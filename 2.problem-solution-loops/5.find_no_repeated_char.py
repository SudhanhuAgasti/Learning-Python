# find the non repeated char in whole string

input_str="teeteraa"

for char in input_str:
    print(char)
    if input_str.count(char)==1:# build in features of python 
        print("Char ehich id not repeated :",char)
        break  # it is only bcz of find the 1st non repeatable char. 

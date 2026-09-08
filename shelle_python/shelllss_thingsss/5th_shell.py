PS D:\PYTHON\ch-1> python
Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> ########## LIST IN PYTHON ##########
>>> tea_varaities=["Black","Green","Oolong","White"]
>>> print(tea_varaities)
['Black', 'Green', 'Oolong', 'White']
>>> print(tea_varaities[1])
Green
>>> print(tea_varaities[-1])
White
>>> print(tea_varaities[1:3])
['Green', 'Oolong']
>>> print(tea_varaities[:2])
['Black', 'Green']
>>> print(tea_varaities[:5])
['Black', 'Green', 'Oolong', 'White']
>>> print(tea_varaities[2:])
['Oolong', 'White']
>>> tea_varaities[3]="Herbal"
>>> print(tea_varaities)
['Black', 'Green', 'Oolong', 'Herbal']
>>> tea_varaities[1:2]
['Green']
>>> tea_varaities[1:2]="Lemon"
>>> tea_varaities[1:2]
['L']
>>> tea_varaities
['Black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'Herbal']
>>> tea_varaities
['Black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'Herbal']
>>> tea_varaities=["Black","Green","Oolong","White"]
>>> tea_varaities
['Black', 'Green', 'Oolong', 'White']
>>> tea_varaities[1:2]
['Green']
>>> tea_varaities[1:2]
PS D:\PYTHON\ch-1> 
 *  History restored 

PS D:\PYTHON\ch-1> python
Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> tea_varaities=["Black","Green","Oolong","White"]
>>> 
>>> tea_varities[1:2]=["lemon"]
Traceback (most recent call last):
  File "<python-input-2>", line 1, in <module>
    tea_varities[1:2]=["lemon"]
    ^^^^^^^^^^^^
NameError: name 'tea_varities' is not defined. Did you mean: 'tea_varaities'?
>>> tea_varaities[1:2]=["lemon"]
>>> tea_varaities
['Black', 'lemon', 'Oolong', 'White']
>>> tea_varaities[1:3]
['lemon', 'Oolong']
>>> tea_varaities[0:3]
['Black', 'lemon', 'Oolong']
>>> tea_varaities[1:3]=["green","white"]
>>> tea_varaities
['Black', 'green', 'white', 'White']
>>> tea_varaities[1:1]
[]
>>> tea_varaities[1:1]=["test,"test]
  File "<python-input-10>", line 1
    tea_varaities[1:1]=["test,"test]
                        ^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> tea_varaities[1:1]=["test","test]
  File "<python-input-11>", line 1
    tea_varaities[1:1]=["test","test]
                               ^
SyntaxError: unterminated string literal (detected at line 1)
>>> tea_varaities[1:1]=["test","test"]
>>> tea_varaities
['Black', 'test', 'test', 'green', 'white', 'White']
>>> tea_varaities[1:2]
['test']
>>> tea_varaities[1:3]
['test', 'test']
>>> tea_varaities[1:3]=[]
>>> tea_varaities[1:3]
['green', 'white']
>>> tea_varaities
['Black', 'green', 'white', 'White']
>>> ###### LOOPING IN LIST ##########
>>> for tea in tea_varaities:
...     print(tea)
...     
Black
green
white
White
>>> for tea in tea_varaities:
...     print(tea,end="-")
...     
>>> k-green-white-White-
>>> for tea in tea_varaities:
...     print(tea,end="-")
...     
>>> k-green-white-White-
>>> tea_varaities
['Black', 'green', 'white', 'White']
>>> if "Oolong" in tea_varaities:
...     print("I have Oolong tea")
...     
>>> if "Oolong" in tea_varaities:
...     print("I have Oolong tea")
...     else:
...         print("I dont have the Oolong Tea")
...         
  File "<python-input-27>", line 3
    else:
    ^^^^
SyntaxError: invalid syntax
>>> tea_varaities.append("Oolong")
>>> tea_varaities
['Black', 'green', 'white', 'White', 'Oolong']
>>> if "Oolong" in tea_varaities:
...     print("I have oolong tea")
...     
I have oolong tea
>>> tea_varaities.pop()
'Oolong'
>>> tea_varaities
['Black', 'green', 'white', 'White']
>>> tea_varaities.push("oolong")
Traceback (most recent call last):
  File "<python-input-34>", line 1, in <module>
    tea_varaities.push("oolong")
    ^^^^^^^^^^^^^^^^^^
AttributeError: 'list' object has no attribute 'push'
>>> tea_varaities.append("oolong")
>>> tea_varaities
['Black', 'green', 'white', 'White', 'oolong']
>>> tea_varaities.remove("green")
>>> tea_varaities
['Black', 'white', 'White', 'oolong']
>>> tea_varaities.remove("white")
>>> tea_varaities
['Black', 'White', 'oolong']
>>> tea_varaities.insert(1,"green")
>>> tea_varaities
['Black', 'green', 'White', 'oolong']
>>> tea_varaities_copy=[tea_varaities]
>>> tea_varaities_copy
[['Black', 'green', 'White', 'oolong']]
>>> tea_varaities_copy=tea_varaities
>>> tea_varaities_copy
['Black', 'green', 'White', 'oolong']
>>> tea_varaities_copy=tea_varaities.copy()
>>> tea_varaities_copy
['Black', 'green', 'White', 'oolong']
>>> ######### here the reference is different
>>> tea_varaities_copy[1:1]=["sudhanshu"]
>>> tea_varaities_copy
['Black', 'sudhanshu', 'green', 'White', 'oolong']
>>> tea_varaities
['Black', 'green', 'White', 'oolong']
>>> ##########loops in list
>>> squared_nums=[x**2 for x in range(10)]
>>> squared_nums
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> ##Explanation of range and other things
>>> range(10)
range(0, 10)
>>> print(range(10))
range(0, 10)
>>> y=range(10)
>>> y
range(0, 10)
>>> squared_nums=[x**2 for x in range(10)]
>>> squared_nums
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> ## Actually it calls list comparsion
>>> cube_nums=[x**3 for x in range(11)]
>>> cube_nums
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
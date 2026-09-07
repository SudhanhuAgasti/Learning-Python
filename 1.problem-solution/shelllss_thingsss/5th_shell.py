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
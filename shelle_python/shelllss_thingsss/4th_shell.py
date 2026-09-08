PS D:\PYTHON\ch-1> python 
Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> ######### STRINGS IN PYTHON #####################
>>> chai="lemon chai"
>>> chai
'lemon chai'
>>> print(chai)
lemon chai
>>> chai = "Masala chai"
>>> chai
'Masala chai'
>>> first_char=chai[0]
>>> first_char
'M'
>>> print(first_char)
M
>>> slice_chai=chai[0:6]
>>> print(slice_chai)
Masala
>>> chai[-1]
'i'
>>> number_list="0,1,2,3,4,5,6,7,8,9"
>>> number_list[]:
  File "<python-input-15>", line 1
    number_list[]:
                ^
SyntaxError: invalid syntax
>>> number_list[:]
'0,1,2,3,4,5,6,7,8,9'
>>> number_list[3:]
',2,3,4,5,6,7,8,9'
>>> number_list[:3]
'0,1'
>>> number_list[0:7:2]
'0123'
>>> num_list="0123456789"
>>> num_list[:]
'0123456789'
>>> num_list[3:]
'3456789'
>>> num_list[:7]
'0123456'
>>> num_list[0:7:2]
'0246'
>>> num_list[0:7:3]
'036'
>>> chai
'Masala chai'
>>> print(chai.lower())
masala chai
>>> print(chai.upper())
MASALA CHAI
>>> chai
'Masala chai'
>>> chai="    masala chai    "
>>> chai
'    masala chai    '
>>> print(chai.strip())
masala chai
>>> print(chai.trim())
Traceback (most recent call last):
  File "<python-input-33>", line 1, in <module>
    print(chai.trim())
          ^^^^^^^^^
AttributeError: 'str' object has no attribute 'trim'. Did you mean: 'strip'?
>>> print(chai.strip())
masala chai
>>> chai="lemon chai"
>>> chai
'lemon chai'
>>> print(chai.replace("lemon","ginger"))
ginger chai
>>> chai
'lemon chai'
>>> chai="Lemon , ginger , Masala, Mint"
>>> print(chai.split())
['Lemon', ',', 'ginger', ',', 'Masala,', 'Mint']
>>> print(chai.split(", "))
['Lemon ', 'ginger ', 'Masala', 'Mint']
>>> chai="Masala 
KeyboardInterrupt
>>> chai = "Masala Chai"
>>> print(chai.find("chai"))
-1
>>> print(chai.find("Chai"))
7
>>> chai = "Masala Chai Chai Chai"
>>> print(chai.count("Chai"))
3
>>> chai_type="Masala"
>>> quantity=2
>>> order="I orderd {} cups of {} chai"
>>> order
'I orderd {} cups of {} chai'
>>> print(order.format(quantity,chai_type))
I orderd 2 cups of Masala chai
>>> chai_variety=["lemon","masala","ginger"]
>>> print(chai_variety)
['lemon', 'masala', 'ginger']
>>> print(''.join(chai_variety))
lemonmasalaginger
>>> print(' '.join(chai_variety))
lemon masala ginger
>>> print('-'.join(chai_variety))
lemon-masala-ginger
>>> print(', '.join(chai_variety))
lemon, masala, ginger
>>> chai ="Masala Chai"
>>> print(len(chai))
11
>>> for letter in chai:
...     print(letter)
...     
M
a
s
a
l
a
 
C
h
a
i
>>> chai = "He said, \"Masala chai is awesome \" "
>>> chai
'He said, "Masala chai is awesome " '
>>> print(chai)
He said, "Masala chai is awesome " 
>>> chai"Masala\n
KeyboardInterrupt
>>> chai="Masala\nChai"
>>> chai
'Masala\nChai'
>>> print(chai)
Masala
Chai
>>> chai = r"masala\nChai"
>>> chai
'masala\\nChai'
>>> print(chai)
masala\nChai
>>> chai = r"c:\\user\\pwd\\"
>>> print(chai)
c:\\user\\pwd\\
>>> chai = r"c:\\user\\pwd"
>>> chai=r"c:\user\pwd"
>>> print(chai)
c:\user\pwd
>>> chai ="Masala chai"
>>> print("masala" in chai )
False
>>> print("Masala" in chai )
True
>>> 
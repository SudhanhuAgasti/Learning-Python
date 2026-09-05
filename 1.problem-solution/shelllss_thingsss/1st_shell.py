PS D:\PYTHON\ch-1> python                                         
Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 12+13
25
>>> 2.5*5
12.5
>>> 2 **3
8
>>> #power
>>> import math
>>> math.pi
3.141592653589793
>>> import random
>>> random.random ()
0.7886480730603864
>>> random.choice([1,2,3,4,5,6])
2
>>> random.choice([12,34,65,34])
>>> username="sudhanhsu"
>>> len(username)
9
>>> 
>>> username=" sudhanshu"
>>> len(username)
10
>>> username[3]
'd'
>>> username="sudhanshu"
>>> username[0]
's'
>>> username[-1]
'u'
>>> useranme[-1]==username[8]
Traceback (most recent call last):
  File "<python-input-26>", line 1, in <module>
    useranme[-1]==username[8]
    ^^^^^^^^
NameError: name 'useranme' is not defined. Did you mean: 'username'?
>>> username[-1]==username[8]
True
>>> username[1:3]
'ud'
>>> dir(username)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> ##listtttttttttttttttttttttttt
>>> mylist=[123,"chai",3.14]
>>> mylist
[123, 'chai', 3.14]
>>> len(mylist)
3
>>> ########   DICTONARY #############
>>>  myD={"a":"lemon","b":"ginger","c":"comic"}
  File "<python-input-35>", line 1
    myD={"a":"lemon","b":"ginger","c":"comic"}
IndentationError: unexpected indent
>>>  myD = {"a":"lemon","b":"ginger","c":"comic"}
  File "<python-input-36>", line 1
    myD = {"a":"lemon","b":"ginger","c":"comic"}
IndentationError: unexpected indent
>>> myD
Traceback (most recent call last):
  File "<python-input-37>", line 1, in <module>
    myD
NameError: name 'myD' is not defined
>>> myD ={'one':'ginger','two':'lemon','three':'tea'}
>>> myD
{'one': 'ginger', 'two': 'lemon', 'three': 'tea'}
>>> myD['three']
'tea'
>>> myD['two']
'lemon'
>>> myD['four']
Traceback (most recent call last):
  File "<python-input-42>", line 1, in <module>
    myD['four']
    ~~~^^^^^^^^
KeyError: 'four'
>>> ##################  TUPPLES  ##############
>>> myTup=(1,2,4)
>>> myTup
(1, 2, 4)
>>> myTup[2]
4
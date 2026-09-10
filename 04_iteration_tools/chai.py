import time

print("Cahi is here !")
username="sudhanshu"
print(username)



# iteration on file system , tupples, dictonary 
PS D:\PYTHON\ch-1\04_iteration_tools> python
Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> f= open('chai.py')
>>> f.readline()
'import time\n'
>>> 
>>> f.readline()
'\n'
>>> f.readline()
'print("Cahi is here !")\n'
>>> f.readline()
'username="sudhanshu"\n'
>>> f.readline()
'print(username)'
>>> f.readline()
''
>>> f.readline()
''
>>> f= open('chai.py')
>>> f.__next__()
'import time\n'
>>> f.__next__()
'\n'
>>> f.__next__()
'print("Cahi is here !")\n'
>>> f.__next__()
'username="sudhanshu"\n'
>>> f.__next__()
'print(username)'
>>> f.__next__()
Traceback (most recent call last):
  File "<python-input-15>", line 1, in <module>
    f.__next__()
    ~~~~~~~~~~^^
StopIteration
>>> for line in open('chai.py'):
...     print(line)
...     
import time



print("Cahi is here !")

username="sudhanshu"

print(username)
>>> for line in open('chai.py'):
...     print(line,end="")
...     
import time

print("Cahi is here !")
username="sudhanshu"
>>> f= open('chai.py')
>>> while True:
...     line=f.readline()
...     if not line:
...         break
...     print(line)
...         
import time



print("Cahi is here !")

username="sudhanshu"

print(username)
>>> test="hitesh"
>>> if not "hitesh":
...     print("hitesh is not here ")
... else:
...     print("hitesh is here !)
...         
...     
...     
  File "<python-input-21>", line 4
    print("hitesh is here !)
          ^
SyntaxError: unterminated string literal (detected at line 4)
>>> if not "hitesh":
...     print("hitesh is not here ")
... else:
...     print("hitesh is here !")
...     
hitesh is here !
>>> myList=[1,2,3,4,5]
>>> I=iter(myList)
>>> 
>>> I
<list_iterator object at 0x0000025D01145ED0>
>>> I.__next__()
1
>>> I
<list_iterator object at 0x0000025D01145ED0>
>>> I.__next__()
2
>>> I.__next__()
3
>>> I.__next__()
4
>>> I.__next__()
5
>>> I.__next__()
Traceback (most recent call last):
  File "<python-input-33>", line 1, in <module>
    I.__next__()
    ~~~~~~~~~~^^
StopIteration
>>> f=open('chai.py')
>>> iter(f) is f
True
>>> iter(f) is f.__iter__
False
>>> iter(f) is f.__iter__()
True
>>> myNewList=[1,2,3]
>>> iter(myNewList) is myNewList
False
>>> ##### DICTIONARY IS ALSO ITERATABLE
>>> D={"a":1,"b":2}
>>> for key in D.keys():
...     print(key)
...     
a
b
>>> # now do this manually 
>>> 
>>> I=iter(D)
>>> I
<dict_keyiterator object at 0x0000025D01237DD0>
>>> next(I)
'a'
>>> 
>>> 
>>> next(I)
'b'
>>> next(I)
Traceback (most recent call last):
  File "<python-input-51>", line 1, in <module>
    next(I)
    ~~~~^^^
StopIteration
>>> range(5)
range(0, 5)
>>> R=range(5)
>>> R
range(0, 5)
>>> I=iter(R)
>>> next(I)
0
>>> next(I)
1
>>> next(I)
2
>>> next(I)
3
>>> next(I)
4
>>> next(I)
Traceback (most recent call last):
  File "<python-input-61>", line 1, in <module>
    next(I)
    ~~~~^^^
StopIteration
>>> 
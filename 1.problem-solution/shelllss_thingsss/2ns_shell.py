PS D:\PYTHON\ch-1> python
Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> ############ INTERNAL WORKING ################
>>> import sys
>>> sys.getrefcount(24601)
3
>>> sys.getrefcount("sudhanshu")
3
>>> sys.getrefcount('sudhanshu')
3
>>> sys.getrefcount('agasti')
3
>>> a=3
>>> a
3
>>> a="sudhanshu"
>>> a
'sudhanshu'
>>> x=a
>>> x
'sudhanshu'
>>> a='agasti'
>>> a
'agasti'
>>> x
'sudhanshu'
>>> a=2
>>> b=3
>>> a+b
5
>>> a=a+b
>>> a
5
>>> c=a
>>> c
5
>>> a=9
>>> c
5
>>> myListOne=[1,2,3]
>>> myListTwo=myListOne
>>> myListOne="chai"
>>> myListTwo
[1, 2, 3]
>>> myListOne
'chai'
>>> myListOne=[1,2,3]
>>> myListTwo
[1, 2, 3]
>>> myListOne
[1, 2, 3]
>>> myListOne[0]=34
>>> myListOne
[34, 2, 3]
>>> myListTwo
[1, 2, 3]
>>> l1=[1,2,3]
>>> l2=l1
>>> l1
[1, 2, 3]
>>> l2
[1, 2, 3]
>>> l1[0]=44
>>> l1
[44, 2, 3]
>>> l2
[44, 2, 3]
>>> p1=[1,2,3]
>>> p2=p1
>>> p2=[1,2,3]
>>> p1[0]=55
>>> p1
[55, 2, 3]
>>> p2
[1, 2, 3]
>>> h1=[1,2,4]
>>> h2=h1[:]
>>> h1
[1, 2, 4]
>>> h2
[1, 2, 4]
>>> h1[0]=89
>>> h1
[89, 2, 4]
>>> h2
[1, 2, 4]
>>> ###   here we not taking the reference we create a copy here in the ab\ove ;
>>> import copy
>>> h2=copy.copy(h1)
>>> h1
[89, 2, 4]
>>> h2
[89, 2, 4]

>>> ## DEEP COPY ##
>>> H1=[1,2,3,4,5]
>>> h1=[1,2,3,4,5]
>>> h1=[1,2,3,[4,5],6]
>>> h2=copy.copy(h1)
>>> h1
[1, 2, 3, [4, 5], 6]
>>> h2
[1, 2, 3, [4, 5], 6]
>>> h2=copy.deepcopy(h1)
>>> h2
[1, 2, 3, [4, 5], 6]

 ######## BEACAUSE OF DIFFERENT OBJECT
>>> n=[1,2,3]
>>> n=m
Traceback (most recent call last):
  File "<python-input-70>", line 1, in <module>
    n=m
      ^
NameError: name 'm' is not defined
>>> m=n
>>> n
[1, 2, 3]
>>> m==n
True
>>> n==m
True
>>> m is n
True
>>> n=[1,2,3]
>>> m=[1,2,3]
>>> n==m
True
>>> n is m
False

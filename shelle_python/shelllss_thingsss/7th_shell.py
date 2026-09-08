>>> ##########  TUPULES IN PYTHON #############
>>> tea_types=("Black","Green","Oolong")
>>> tea_types
('Black', 'Green', 'Oolong')
>>> tea_types[0]
'Black'
>>> tea_types[-1]
'Oolong'
>>> tea_types[1:]
('Green', 'Oolong')
>>> tea_types[0]
'Black'
>>> tea_types[0]="Lemon"
Traceback (most recent call last):
  File "<python-input-7>", line 1, in <module>
    tea_types[0]="Lemon"
    ~~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
>>> tea_types[0]=["Lemon"]
Traceback (most recent call last):
  File "<python-input-8>", line 1, in <module>
    tea_types[0]=["Lemon"]
    ~~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
>>> len(tea_types)
3
>>> more_tea=("Harbel","Earl Grey")
>>> all_tea=more_tea+tea_types
>>> all_tea
('Harbel', 'Earl Grey', 'Black', 'Green', 'Oolong')
>>> if "Green" in all_tea:
...     print("I have green tea")
...     
I have green tea
>>> more_teaa=("Herbel","Earl grey","Herbel")
>>> more_tea=("Herbel","Earl grey","Herbel")
>>> more_tea
('Herbel', 'Earl grey', 'Herbel')
>>> more_tea.count("Herbel")
2
>>> more_tea.count("Herbe")
0
>>> tea_types
('Black', 'Green', 'Oolong')
>>> (black,green,oolong)=tea_types
>>> black
'Black'
>>> green
'Green'
>>> oolong
'Oolong'
>>> ("",(1,2,3),"")
('', (1, 2, 3), '')
>>> ## nested tuples
>>> 
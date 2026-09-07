 python
Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> ###### DICTIONARY  #############
>>> chai_types={"Masala":"Spicy","Ginger":"Zesty","Green":"Mild"}
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
>>> ####  How to access the individuals value and key
>>> chai_types["Masala"]
'Spicy'
>>> chai_types["Masala"]
'Spicy'
>>> chai_types.get("Ginger")
'Zesty'
>>> chai_types.get("Gingery")
>>> chai_types["Masala"]
'Spicy'
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
>>> chai_types["Green"]=["Fresh"]
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': ['Fresh']}
>>> chai_types["Green"]="Fresh"
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
>>> ########### Loops in dictionary
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
>>> for chai in chai_types:
...     print(chai)
...     
Masala
Ginger
Green
>>> for chai in chai_types:
...     print(chai,chai_types[chai])
...     
Masala Spicy
Ginger Zesty
Green Fresh
>>> for key,values in chai_types.items():
...     print(key,value)
...     
Traceback (most recent call last):
  File "<python-input-20>", line 2, in <module>
    print(key,value)
              ^^^^^
NameError: name 'value' is not defined. Did you mean: 'values'?
>>> for key,value in chai_types.items():
...     print(key,value)
...     
Masala Spicy
Ginger Zesty
Green Fresh
>>> if "Masala" in chai_types:
...     print("I have masala chai")
...     
I have masala chai
>>> print(len(chai_types))
3
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
>>> chai_types["Earl Grey"]=""
KeyboardInterrupt
>>> chai_types["Earl Grey"]="Citrus"
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}
>>> chai_types.pop("Ginger")
'Zesty'
>>> chai_types
{'Masala': 'Spicy', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}
>>> chai_types.popitem()
('Earl Grey', 'Citrus')
>>> chai_types
{'Masala': 'Spicy', 'Green': 'Fresh'}
>>> del chai_types["Green"]
>>> chai_types
{'Masala': 'Spicy'}
>>> chai_types_copy=chai_types.copy()
>>> chai_types_copy
{'Masala': 'Spicy'}
>>> chai_types_copy["name"]="sudhanshu"
>>> chai_types_copy
{'Masala': 'Spicy', 'name': 'sudhanshu'}
>>> chai_types
{'Masala': 'Spicy'}
>>> tea_shop={}
>>> tea_shop={
... "chai":{"Masala":"Spicy","Ginger":"Zesty"},
... "tea":{"Green":"Mild","Black":"Strong"}
... }
>>> tea_shop
{'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'tea': {'Green': 'Mild', 'Black': 'Strong'}}
>>> tea_shop[chai]
Traceback (most recent call last):
  File "<python-input-41>", line 1, in <module>
    tea_shop[chai]
    ~~~~~~~~^^^^^^
KeyError: 'Green'
>>> tea_shop["tea"]
{'Green': 'Mild', 'Black': 'Strong'}
>>> tea_shop["chai"]
{'Masala': 'Spicy', 'Ginger': 'Zesty'}
>>> tea_shop["chai"]["Ginger"]
'Zesty'
>>> sqared_num={x:x**2 for x in range(6)}
>>> sqared_num
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
>>> keys=["Masala","Ginger","Lemon"]
>>> keys
['Masala', 'Ginger', 'Lemon']
>>> default_value="Delicious"
>>> new_dict= dict.fromkeys(keys,default_value)
>>> new_dict
{'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}
>>> new_dict= dict.fromkeys(keys,key)
>>> new_dict
{'Masala': 'Green', 'Ginger': 'Green', 'Lemon': 'Green'}
>>> new_dict= dict.fromkeys(keys,keys)
>>> new_dict
{'Masala': ['Masala', 'Ginger', 'Lemon'], 'Ginger': ['Masala', 'Ginger', 'Lemon'], 'Lemon': ['Masala', 'Ginger', 'Lemon']}
>>> 
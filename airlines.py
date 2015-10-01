# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 18:49:02 2015

@author: Kruthika
"""

x = 5
y  = "hello"
z = 5.6

x*y


#a = [1,2,3]

#b= [7, 8, 9]

#a+b

cart = [{"name": "banana" , "price" : 0.89}, {"name": "grapes", "price":1.89}]

for cart_item in cart:
    print(cart_item['name'], cart_item['price']< 1.00)

cart.append({"name" : "cookie", "price" : 0.59})
cart.reverse()
#cart.count()

cart[0:2]

banana = {"name": "banana" , "price" : 0.89}
banana.keys()
banana.values()

#for (key, value) in banana.keys():
    #value = banana[key]
    #print(key,value)
    
for (key, value) in banana.items():
    #value = banana[key]
    print(key,value)
    
banana.items() #Groupings of key and value

numbers = [1,2,3,4,5]

[(n, n<4) for n in numbers]


[n for n in numbers if n%2 ==0] # List comprehension

new_numbers = []
for n in numbers:
    for m in range(n):
        new_numbers.append(m)
new_numbers

a="TeXt is BuTTchered".lower().split()

if "owl" in a:
    print("Hoo")
else :
    print("Read")

new_numbers = []
for n in numbers:
    if n%2 == 0:
        new_numbers.append(n)
new_numbers

def g(t):
     
def f(a):
    print(a)
    a("hello")
f(g)






    
    
    
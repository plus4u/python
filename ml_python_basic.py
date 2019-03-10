# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 19:01:26 2019
 
print(123 + 1)

print(10)

print(0o10)

type(10)

type(0o10)

4.2

type(4.2)

4.2e-4

print("I am a string.") 
type("I am a string.")

print('foo\tbar')

type(True)

abs(-10.7)

any([1, 2, 3, 0])

eval('1+2')

eval("'hi' + 'abc'")

eval('divmod(7, 3)')

divmod(7, 3)
 
7 // 3

7 % 3

a = input()

a


list("python")


# two_times.py  
def two_times(numberList):
    result = [ ]
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1, 2, 3, 5])
print(result)

# function two_times vs function map
def two_times(x): 
     return x*2

list(map(two_times, [1, 2, 3, 5]))

#
money = 5000
if money >= 3000:
     print("take a taxi to go")
else:
     print("walk")
 
    
##

treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("I've got a tree cut %d" % treeHit)
    if treeHit == 10:
         print("tree falls")

## 
test_list = ['one', 'two', 'three'] 
for i in test_list: 
    print(i)

# 
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)    

#
    
"I eat %d apples." % 5
    
"I eat %s apples." % "five"

number = 3

"I eat %d apples." % number

"I eat %s apples." % "five"

"%10s" % "hi"

"I eat {0} apples".format(3)
 
y = 3.42134234
"{0:0.4f}".format(y)

## class

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))

## class
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

#
a = FourCal()
a.setdata(4, 2)
a.add()

#
b = FourCal()
b.setdata(3, 7)
b.add()


## constructor

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result 

a = FourCal(4, 2)
a.add()

##  current working directory : C:\Users\beomc
import os
cwd = os.getcwd()
print(os.getcwd() + "\n")

os.chdir('C://Users/beomc/working')
cwd = os.getcwd()
print(os.getcwd() + "\n")


## import

import python_mod1

print(python_mod1.add(3, 4))


from mod1 import add, sub

    


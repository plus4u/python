## 

a = {1: 5, 2: 3}
a[1]
b = {'abc' : 1, 'def' : 2}
b['abc']

a = {'kim': [1, 2, 3], 'lee': 20, 'park': 15, 'suzy': 30}
a['kim']

for key in a:
     print(key)
     
for val in a.values():
     print(val)

t = (1, "korea", 3.5, 1)

i=0
for val in t :
     print(t[i])



my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

my_list 
print(my_tuple)

my_list[0]  # 1
my_tuple[0]  # 1

for i in my_list : 
   print(i)

my_list[0] = "Hello" 
my_list # various_list = ["Hello", 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_tuple[0] = "Hello"  # TypeError: 'tuple' object does not support item assign


a = [(1,2), (3,4), (5,6)]

for (first, last) in a:
     print(first + last)


###
import random

class Exa_1 : 
    face_no = 7         
    def shoot(self) :
        return random.randint(1, 7)


## 
ju = Exa_1()
 
ju.shoot()

 
##
import exa_1

ju=exa_1.Exa_1()

ju.shoot()

##

class Exa_2() : 
    face_no = 9         
    def shoot(self) :
        return random.randint(1, 7)


Exa_2.face_no 

Exa_2.shoot(1)
    
##

import random
class Dice :
    def __init__ (self, val=6):
        self.face_no = val
        print ("hello")
    def  shoot ( self ) :
        return random.randint(1, self.face_no )

ju = Dice(100)  # hello 
ju.shoot()   

##

class Complex:
     def __init__(self, realpart, imagpart):
         self.r = realpart
         self.i = imagpart

x = Complex(3.0, -4.5)

x.r
x.i


## module test 
    


##

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)

x.counter

x.f()


del x.counter


## 
a ='c'

print("개행 \n", " 개행후 ", a)

##

a = int(input())
if a ==1 :
    print("일 입니다.")
elif a==3:
    print("삼 입니다.")
else:
    print("값이 없습니다.")

##


# sys.path.insert(0, "C:\Users\gwihy\ML_01")

sys.path.append('\work')

import tempo_module as mo

mo.triple(3)

import os
os.getcwd()

from os import chdir

chdir('C:\work\sample')
##

import temp as te

te.mo_fuc(4)

os.listdir('.') 

##

import mo_dice as mm


jusawi = mm.Dice()

jusawi.shoot()

## 

reload(mo_dice) 

import mo_dice as mm

jusawi = mm.Dice2()

jusawi.shoot()

##
import mo_dice as mm

jusawi = mm.Dice2(4)

jusawi.shoot()


##

class myClass1(object):
    def __init__(self, *args, **kwargs):
        #args -- 이름이 없는 인자를 저장하는 tuple
        # #kwargs -- 이름이 있는 인자를 저장하는 dict
        print("aargs:", args)
        print("kwargs:", kwargs)
        mynum = 3 if kwargs['num'] is None else kwargs['num']

o = myClass1(1,2, 3, "hello", num = 1, mystring = "mystring")

o = myClass1(num=0)

o = myClass1()


##

t1 ='blog 1'
t2 ='sns'
t3 ='facebook'

def my_arg(*test):
    for post in test :
        print(post)

my_arg(t1, t2, t3)     

def a(*args):
    print(args)

a(1,2,3,4) #  (1,2,3,4)

def b(**kwargs):
    print(kwargs)

b( a=1, b=2, c=3)

def a(fst, *others):
    print ("1st :", fst)
    for arg in others:
        print ("other parameter: ", arg)

a('kim', 'lee', 'ok', 'test')

#
def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items(): 
            print("%s == %s" % (key, value))  
            
greet_me(name="ok")

##
# *args의 첫번째

def test_args_kwargs(arg1, arg2, arg3):
        print ("k1 :", arg1)
        print ("k2 :", arg2)
        print ("k3 :", arg3)
        
args = ("two", 3, 5)
test_args_kwargs(*args) 


# 이제 **kwargs:
kwargs = {"k3" : 3, "k2" : "two", "k1" : 5}  
kwargs 

test_args_kwargs(**kwargs)
 
        
        
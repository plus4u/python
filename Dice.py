# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 21:47:45 2019

@author: gwihy
"""



import random

class Dice : 
    face_no = 7         
    def shoot(self) :
        return random.randint(1, 7)


ju = Dice()

ju.shoot()







import random

class Dice : 
    def __init__(self, val) : 
        self.face_num = val
        
    def shoot(self) :
        return random.randint(1, self.face_num)




ju = Dice(4)

ju = Dice.shoot(2)

## class

class Myclass(object):
# class Myclass :
    def __init__(self, num = 3):
        self.myvalue = num
        return print('hello')

ins1 = Myclass()
# ins1 = Myclass

print(ins1)
        
##

class MyClass1(object):
    def __init__(self, *args, **kwargs):
        #args -- 이름이 없는 인자를 저장하는 tuple
        # #kwargs -- 이름이 있는 인자를 저장하는 dict
        
        print("aargs:", args)
        print("kwargs:", kwargs)
        mynum = 3 if kwargs['num'] is None else kwargs['num']

o = MyClass1(3, "hello", num = 1, mystring = "mystring")


x = 100
id(x)

y =100
id(y)






    
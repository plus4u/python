# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 07:47:24 2019

class, module 

@author: gwihy
"""

##
class robot:
  name = "robot"
  def info(self):
    print('나의 이름은', self.name, '입니다!')
 
    
r = robot()

type(r)

r.info()

r.name


##

class robot:
  name = "robot"
  age = 0
  def __init__(self, name, age):
    print('생성자 호출!')
    self.name = name
    self.age = age
  def __del__(self):
    print('소멸자 호출!')
  def info(self):
    print('나의 이름은', self.name, '입니다!')
    print('나이는', self.age, '입니다!')
    
    
r = robot

r.info

##

class robot:
  name = 'robot'
  age = 0
  def __init__(self, name, age):
    print('robot 생성자 호출!')
    self.name = name
    self.age = age
  def __del__(self):
    print('robot 소멸자 호출!')
  def info(self):
    print('나의 이름은', self.name, '입니다!')
    print('나이는', self.age, '입니다!')

class strong_robot(robot):
  weapon = 'gun'
  def __init__(self, name, age, weapon):
    print('strong_robot 생성자 호출!')
    super().__init__(name, age)
    self.weapon = weapon
  def info(self): #오버라이딩
    super().info()
    print(self.weapon, '로 싸웁니다!')
    
    
    
    
    ##
    
class test:
    data = 10
    

t = test

t.data

#

class test:
    __data = 10
    def getData(self):
        return self.__data
    def setData(self, data):
        self.__data = data


t = test()

t.getData()

t.setData(23)

##

class test:
    data = 10 # 클래스 속성
    def __init__(self, data): 
        self.data = data # 인스턴스 속성
    @classmethod
    def printClass(cls): # 클래스 메소드
        print(cls.data)
        
    def printInstance(self): # 인스턴스 메소드
        print(self.data)
   
t = test(33)
     
test.data

t.data

t.printClass()

t.printInstance()

test.printClass()

##



import random

class Dice() : 
    def __init__(self, val=6) : 
        self.face_num = val
        
    def shoot(self) :
        return random.randint(1, self.face_num)



ju = Dice()

ju.face_num


##

def fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b, a+b
    return a

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(fibonacci(6))
 

        

    






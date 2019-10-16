# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 20:41:14 2019

@author: gwihy
"""

class MyCar():
    engine = 0 # 클래스 변수

    def __init__(self, speed, tire): # 생성자
        # self.* # 인스턴스 변수
        self.speed = speed
        self.tire = tire
        MyCar.engine += 1


    @staticmethod
    def is_engine(speed1, speed2):
            return speed1 == speed2


    @classmethod
    def get_engine(cls):
      return cls.engine


my_car = MyCar(5, '한국')  

print(my_car.speed) # 5
print(my_car.tire) # 한국
print(my_car.get_engine()) # 1
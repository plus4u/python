# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 11:00:46 2019

@author: gwihy
"""

import turtle    # 상속을 받았기 때문에, 기본 모듈을 불러와야 합니다. 
 
class Turtle_new(turtle.Turtle):
    def box(self, pos_x, pos_y, x, y, color):
        self.penup()
        self.goto(pos_x - x/2,pos_y - y/2) 
        self.pendown()
        self.speed('fast')
        self.color(color)
        self.begin_fill()
        self.fd(x)
        self.left(90)
        self.fd(y)
        self.left(90)
        self.fd(x)
        self.left(90)
        self.fd(y)
        self.left(90)
        self.end_fill()


##
 

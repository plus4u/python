# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 20:50:57 2019

@author: gwihy
"""

class Calculator:

	def __init__(self):

		self.AddCount = 0

		self.MinCount = 0

		self.MulCount = 0

		self.DivCount = 0



	def Add(self, num1, num2):

		self.AddCount = self.AddCount + 1

		return num1 + num2



	def Min(self, num1, num2):

		self.MinCount = self.MinCount + 1

		return num1 - num2



	def Mul(self, num1, num2):

		self.MulCount = self.MulCount + 1

		return num1 * num2



	def Div(self, num1, num2):

		self.DivCount = self.DivCount + 1

		return num1 / num2



	def ShowCount(self):

		print("덧셈 : %s" %self.AddCount)

		print("뺄셈 : %s" %self.MinCount)

		print("곱셈 : %s" %self.MulCount)

		print("나눗셈 : %s" %self.DivCount)
        
        
        
cal = Calculator()

print("10 + 20 = %s" %cal.Add(10,20))

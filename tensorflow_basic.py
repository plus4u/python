# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 21:58:37 2019

@author: beomc
"""

import tensorflow as tf

x = tf.constant([1.8, 2.2], dtype=tf.float32)
tf.cast(x, tf.int32)  # [1, 2], dtype=tf.int32

x1 = tf.cast(x, tf.int32)


print(x1)

# import functions

a1 = tf.Variable([0.1, 0.3, 0.5])
print(a1)

# functions.showOperation(tf.argmax(a1, 0))

## 

a = tf.constant([3, 10, 1])

session = tf.Session()

print('a:\n', session.run(a))
print('rank = index 의 개수 = ', session.run(tf.rank(a)) )
print('tf.argmax(a, 0): index ', session.run(tf.argmax(a, 0)), '이 가장 큽니다.')

##

a = tf.constant([[3, 10, 1],[4, 5, 6],[0, 8, 7]])

session = tf.Session()
print('a:\n', session.run(a))
print('인덱스의 개수 = ', session.run(tf.rank(a)))
print('tf.argmax(a, 0): 인덱스 ', session.run(tf.argmax(a, 0)), '가 가장 큽니다.')
print('tf.argmax(a, 1): 인덱스 ', session.run(tf.argmax(a, 1) ), '가 가장 큽니다.')

# Python program to print list 
# using for loop 
a = [1, 2, 3, 4, 5] 
  
# printing the list using loop 
for x in range(len(a)): 
    print(a[x], end="\n") 


# printing the list using * operator separated  
# by space
print(a)
print(*a) 
  
# printing the list using * and sep operator 
print("printing lists separated by commas") 
  
print(*a, sep = ", ")  
  
# print in new line 
print("printing lists in new line") 
  
print(*a, sep = "\n") 


 # Python program to print list 
# by Converting a list to a  
# string for display 
a =["Geeks", "for", "Geeks"] 
  
# print the list using join function() 
print(' '.join(a)) 
  
# print the list by converting a list of  
# integers to string  
a = [1, 2, 3, 4, 5] 
  
print(str(a)[1:-1])  

print(a[1:-1])  

#
import tensorflow as tf
b = 3

b_one_hot = tf.one_hot(b, 7)

print(b_one_hot)

b = [0, 0, 0, 1, 0]
import numpy as np
np.argmax(b)

print(tf.argmax(b))   # error

c = tf.argmax(b)
print(b)
print(c)
c


with tf.Session() as sess: 
    sess.run(tf.argmax(b))
    
    
#
import numpy as np
listy = [7, 6, 5, 7, 6, 7, 6, 6, 6, 4, 5, 6]
winner = np.argwhere(listy == np.amax(listy))
print(winner) 

print(winner.flatten().tolist()) # if you want it as a list

##

a = np.arange(6).reshape(2,3)
a
 
np.argmax(a)

#
np.argmax(a, axis=0)
 
np.argmax(a, axis=1)

b = np.arange(6)
b
b[1] = 5
b
 
np.argmax(b) # Only the first occurrence is returned.

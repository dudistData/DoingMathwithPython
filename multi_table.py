# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 21:39:03 2019

@author: wilki
"""
def multi_table(a):
      for i in range(1, 11):        
          print('{0} x {1} = {2}'.format(a, i, a*i))
      while True:     
           a = input('Enter a number: ')        
           multi_table(float(a)) 
           
           answer = input('Do you want to exit? (y) for yes ')        
           if answer == 'y':           
               break
multi_table(9)

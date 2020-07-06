# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 01:22:42 2020

@author: fatemeh
"""

# A basic code for matrix input from user 
  
R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
  
# Initialize matrix 
matrix = [] 
print("Enter the entries rowwise:") 
  
# For user input 
for i in range(R):          # A for loop for row entries 
    a =[] 
    for j in range(C):      # A for loop for column entries 
         a.append(int(input())) 
    matrix.append(a) 
  
# For printing the matrix 
for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end = " ") 
    print() 

import numpy as np


matrix = np.array(matrix)
Ainv = np.linalg.inv(matrix)
print(Ainv)
    
    

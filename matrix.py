# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 01:22:42 2020

@author: fatemeh
"""
import numpy as np

def InverseMatrix(A):
    A = np.array(A)
    Ainv = np.linalg.inv(A)
    print(Ainv)
    
    
InverseMatrix(([1,3,3],[1,4,3],[1,3,4]))
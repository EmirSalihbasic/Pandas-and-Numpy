# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 11:25:45 2023

@author: Korisnik
"""
import numpy as np
#open mona lisa text file
f = open("C:/Users/Korisnik/Desktop/Ex_Files_Python_Data_Analysis/Exercise Files/chapter4/monalisa.txt", "r")
print(f.read())
    
monalisa = np.loadtxt("C:/Users/Korisnik/Desktop/Ex_Files_Python_Data_Analysis/Exercise Files/chapter4/monalisa.txt")

print(monalisa)

print(monalisa.ndim)

print(monalisa.shape)

print(monalisa.size)

print(monalisa.dtype)

import matplotlib.pyplot as pp
pp.imshow(monalisa)    #picture of mona lisa in plits

pp.imshow(monalisa, cmap='gray')

monalisa = np.load('C:/Users/Korisnik/Desktop/Ex_Files_Python_Data_Analysis/Exercise Files/chapter4/monalisa.npy')

print(monalisa.shape)

pp.figure(figsize=(5,8))  # later
pp.imshow(monalisa)

fromlist = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(fromlist)

zero_1d = np.zeros(8, 'd') # or np.float64
zero_2d = np.zeros((8,8), np.float64)
zero_1d, zero_1d.ndim, zero_1d.shape, zero_1d.size
zero_2d, zero_2d.ndim, zero_2d.shape, zero_2d.size
print(np.zeros_like(monalisa))

np.empty(24, 'd')

linear = np.linspace(0, 1, 16)

print(linear)

pp.plot(linear, 'o')

np.arange(0, 1.5, 0.1)

rand_2d = np.random.random(size=(8,8))

print(rand_2d)

pp.matshow(rand_2d)

np.random.randint, np.random.randn

np.save('random.npy', rand_2d)

np.savetxt('random.txt', rand_2d)

open('random.txt', 'r').readlines()
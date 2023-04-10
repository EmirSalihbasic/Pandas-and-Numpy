# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 14:13:24 2023

@author: Korisnik
"""

import math
import numpy as np
import matplotlib.pyplot as pp


y=math.pi
print(y)

y2=np.linspace(1*1 ,1)
print(y2)

y3=np.linspace(1*2, 1)
print(y3)

x = np.linspace(0,5*math.pi,64)
print(x)

sinx = np.sin(x)

print(sinx)

pp.plot(x, sinx)

# multiple matplotlib.pyplot.plot() instructions superimpose lines
# in the same plot, cycling colors so we can distinguish them

pp.plot(x, sinx)
pp.plot(x, np.cos(x))
pp.plot(x, np.log(1 + x))

# plot labels can be shown with matplotlib.pyplot.legend()

pp.plot(x, sinx, label='sin(x)')
pp.plot(x, np.cos(x), label='cos(x)')
pp.plot(x, np.log(1 + x), label='log(1+x)')

pp.legend()

cosx = np.cos(x)

y = sinx * cosx
z = cosx**2 - sinx**2

pp.plot(x, y)
pp.plot(x, z)

x + y[16:32]

w = sinx + 1.5

sinx[:10]

w[:10]

pp.plot(x, sinx)
pp.plot(x, w)

monalisa_bw = np.loadtxt('monalisa.txt')

monalisa_bw.shape

xgrad = np.linspace(0, 1, 134)

monalisa_xgrad = monalisa_bw * xgrad

# set nominal figure size in inches; show images in two adjacent subplots

pp.figure(figsize=(8,5))
pp.subplot(1,2,1); pp.imshow(monalisa_bw, cmap='gray')
pp.subplot(1,2,2); pp.imshow(monalisa_xgrad, cmap='gray')

ygrad = np.linspace(0, 1, 200)

ygrad * monalisa_bw

ygrad = ygrad[:, np.newaxis]

ygrad.shape

monalisa_ygrad = monalisa_bw * ygrad

pp.figure(figsize=(8,5))
pp.subplot(1,2,1); pp.imshow(monalisa_bw, cmap='gray')
pp.subplot(1,2,2); pp.imshow(monalisa_ygrad, cmap='gray')

a = np.array([0,1,2])

b = np.array([-1,-2,-3])

a @ b

np.dot(a, b)

C = np.random.randn(3, 3)

C

C @ a
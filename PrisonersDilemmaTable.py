# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 03:13:48 2023

@author: Korisnik
"""

import numpy as np
import pandas as pd

#payoffs with numpy array
x = np.array([[-1, -10],[0, -9]])


# re-label the rows and columns
jpm=pd.DataFrame(x, columns=['dove', 'hawk'])
jpm.index = ['dove', 'hawk']
jpm
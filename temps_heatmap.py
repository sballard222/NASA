# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 13:26:30 2017

@author: jmh5ad
"""
import numpy as np
import seaborn as sb
from matplotlib import pyplot as plt
import pandas as pd

filename="Cville_temps.csv"
data = pd.read_csv(filename)

#  To loop at a heatmap, but we need 
#  the data in the format of a numpy array.
temps = np.array(data.ix[:, 1:].values, dtype=float)

#   Can use xticklabels argument in heatmap for x-axis
sb.heatmap(temps, xticklabels=data.columns[1:])

#  The labels of the y-axis are only the row
#  numbers.  Let's change them to the years.
#  But, I only want to display every third one to
#  keep the axis a little cleaner.
numRows = temps.shape[0]
years = data.values[:, 0]
label_ndx = np.arange(0, numRows, 3)

plt.yticks(label_ndx, years[label_ndx][::-1])
plt.show()

#  *****************************
#  Observations:
#  *****************************
#  In general, 17 June is hotter than 
#  the days in May.
#  It also is interesting that 14 May had
#  increased integers in 1985, 1991, 2004, and 2010.
#  Could there by a 6 - 8 year cycle?
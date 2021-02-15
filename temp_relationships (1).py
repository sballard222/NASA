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
temps = data.values[:,1:]


sb.set(style='ticks', color_codes=True)
sb.pairplot(data)

#  *****************************
#  Observations:
#  *****************************
#   The histograms don't reveal much.  This
#   could be due to a relatively small data 
#   size.  May 16th seems to be the closest 
#   to a uniform distribution.  June 17th 
#   seems to be divided between values less 
#   than 70 degrees and values greater than 
#   70 degrees.
#   The only scatter plot that has a visible
#   pattern is the May 15th/May 16th plot.  
#   These two dates tend toward a linear 
#   relationship.
#  

sb.lmplot("15-May", "16-May", data=data)

#  *****************************
#  Observations:
#  *****************************
#  Overall, the higher the temperature is
#  on 15 May, the higher it will be the next
#  day.  There is one clear outlier where the
#  temperature was in the 70s on the 15th and
#  in the 50s on the 16th.  Interesting, let's
#  find the year when this happens.

May16 = "16-May"
May15 = "15-May"

ndx_May16 = list(np.where(data[May16] < 55))[0]

ndx = list(np.where(data[May15].iloc[ndx_May16] > 70))[0]
yeaOfInterest = data.loc[ndx]


#  *****************************
#  Observations:
#  *****************************
#  Interesting, just big jumps in the temperatures 
#  each day for that year.



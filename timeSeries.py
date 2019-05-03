#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 16:28:17 2019

@author: spulford
"""

#%matplotlib notebook
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("timeseries_raw_corrected.csv")


#Creates plot visual
plt.figure(figsize = (10,4), facecolor=None)
ax=plt.gca()
ax.set_facecolor('white')
#lines for online and face to face

plt.plot(df["Year"], df["Face-to-Face Average"],  '-', zorder = 2, 
         color="black", linewidth = 1.0, alpha=0.4, 
         label='In-Person Average', linestyle="dashed")
plt.plot(df["Year"], df["Online Average"], '-', 
         zorder = 2, color="blue", linewidth = 1.0, alpha=0.4, 
         label='Online Average', linestyle="dashed")

plt.plot(df["Year"], df["Face-to-Face Weighted"],  '-', zorder = 2, 
         color="black", linewidth = 1.0, alpha=0.6, 
         label='In-Person Weighted')
plt.plot(df["Year"], df["Online Weighted"], '-', 
         zorder = 2, color="blue", linewidth = 1.0, alpha=0.6, 
         label='Online Average')



# fill the area between the weighted values
plt.gca().fill_between(df["Year"], 
                       df["Face-to-Face Weighted"], df["Online Weighted"], 
                       facecolor='black', 
                       alpha=0.25, zorder = 1, label='_nolegend_')


#Formatting
plt.title("Average Grades in SAS25V, In Person and Online", alpha=0.8)
for spine in plt.gca().spines.values(): spine.set_visible(False)
plt.tick_params(bottom=False, left=False)

plt.yticks(alpha = 0.8)
plt.xticks(alpha = 0.8)
plt.legend(fontsize='xx-small', loc=1, frameon=False)
#plt.ylim(70, 100)
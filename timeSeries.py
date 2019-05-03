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




plt.plot(df["Year"], df["Face-to-Face Average"],  '-', marker=".", zorder = 2, 
         color="#5B7F95", linewidth = 1.0, alpha=0.4, 
         label='In-Person Average', linestyle="dashed")
plt.plot(df["Year"], df["Face-to-Face Weighted"],  '-', marker=".", zorder = 2, 
         color="#5B7F95", linewidth = 3.0, alpha=0.6, 
         label='In-Person Weighted Average')

plt.plot(df["Year"], df["Online Average"], '-', marker=".",
         zorder = 2, color="#008EAA", linewidth = 1.0, alpha=0.4, 
         label='Online Average', linestyle="dashed")
plt.plot(df["Year"], df["Online Weighted"], '-', marker=".",
         zorder = 2, color="#008EAA", linewidth = 3.0, alpha=0.6, 
         label='Online Weighted Average')




# fill the area between the weighted values
plt.gca().fill_between(df["Year"], 
                       df["Face-to-Face Weighted"], df["Online Weighted"], 
                       facecolor='#F0DD99', 
                       alpha=0.5, 
                       zorder = 1, label='_nolegend_')


#Formatting
plt.title("Average Grades in SAS25, In Person and Online", alpha=0.8)
for spine in plt.gca().spines.values(): spine.set_visible(False)
plt.tick_params(bottom=False, left=False)

plt.yticks([76, 78, 80, 82, 84, 86, 88, 90, 92], 
           ["76%", "78%", "80%", "82%", "84%", "86%", "88%", "90%", "92%"], 
           alpha = 0.8)
plt.xticks(alpha = 0.8)
plt.legend(fontsize='xx-small', loc=1, frameon=False)
#plt.ylim(70, 100)
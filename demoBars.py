#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 15:30:35 2019

@author: spulford
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc #set rc params https://matplotlib.org/api/_as_gen/matplotlib.pyplot.rc.html
#from matplotlib.ticker import FuncFormatter


#defining a few functions I'll use



def makePercent(df = dfGender):
    divBy = np.sum(df, axis=1)
    df = df.divide(divBy, axis = 'rows')
    return df;



#set up data frames using demographic numbers

Online = {"Women":238, "Men":178, "Seniors":166, "Non-Seniors":251, 
          "English Only":192, "English and Another":108, "Another Language":117}
inPerson = {"Women":316, "Men":320, "Seniors":91, "Non-Seniors":545, 
          "English Only":350, "English and Another":143, "Another Language":143}

dfGender = pd.DataFrame([inPerson, Online], columns=["Men", "Women"], 
                        index=["In Person", "Online"])


dfStanding = pd.DataFrame([inPerson, Online], columns=["Non-Seniors", "Seniors"], 
                        index=["In Person", "Online"])

dfESL =  pd.DataFrame([inPerson, Online], columns=["English Only", 
                      "English and Another", "Another Language"], 
                        index=["In Person", "Online"])

dfGender = makePercent(dfGender)
dfStanding = makePercent(dfStanding)
dfESL = makePercent(dfESL)

#a couple of tests of basic percent stacked barplots
#using https://python-graph-gallery.com/13-percent-stacked-barplot/ for reference

#Have to normalize bars by total.


#Testing gender distribution stacked bars:
barWidth = 0.85
#names
plt.bar([0, 1], dfGender["Men"], color='darkcyan', edgecolor='white', width=barWidth)
plt.bar([0,1], dfGender["Women"], bottom=dfGender["Men"], color='powderblue', 
        edgecolor='white', width=barWidth) 
#removing frame and ticks
for spine in plt.gca().spines.values(): spine.set_visible(False)
plt.tick_params(bottom=False, left=False)   
plt.xticks([0, 1], ["In Person", "Online"])
plt.legend(loc='upper left', bbox_to_anchor=(1,1), ncol=1) 
        
        
plt.show()

plt.bar([0, 1], dfStanding["Non-Seniors"], color='darkcyan', edgecolor='white', 
        width=barWidth)
plt.bar([0, 1], dfStanding["Seniors"], bottom=dfStanding["Non-Seniors"], 
        color='powderblue', edgecolor='white', width=barWidth)  

#removing frame and ticks
for spine in plt.gca().spines.values(): spine.set_visible(False)
plt.tick_params(bottom=False, left=False) 

plt.xticks([0, 1], ["In Person", "Online"]) 
           
plt.show()

#Trouble: need process for third bar.
plt.bar([0, 1], dfESL["English Only"], color='darkcyan', edgecolor='white', width=barWidth)
plt.bar([0, 1], dfESL["English and Another"], bottom=dfESL["English Only"], 
        color='cadetblue', edgecolor='white', width=barWidth)     
barBottom = np.add(dfESL["English Only"], dfESL["English and Another"]).tolist()
plt.bar([0, 1], dfESL["Another Language"], bottom=barBottom,
        color='powderblue', edgecolor='white', width=barWidth)
#removing frame and ticks
for spine in plt.gca().spines.values(): spine.set_visible(False)
plt.tick_params(bottom=False, left=False) 
 
plt.xticks([0, 1], ["In Person", "Online"])  
plt.show()

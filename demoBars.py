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
from matplotlib.ticker import FuncFormatter
#from matplotlib.pyplot import fig


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

fig = plt.figure()

ax1 = fig.add_subplot(3, 1, 1)
ax1.barh([0, 1], dfGender["Men"], color='darkcyan', edgecolor='white', height=barWidth)
ax1.barh([0, 1], dfGender["Women"], left=dfGender["Men"], color='powderblue', 
         edgecolor='white', height=barWidth) 
#removing frame and ticks
for spine in plt.gca().spines.values(): spine.set_visible(False) 
plt.tick_params(axis='x', labelbottom=False)
#should make object oriented coding consistent here
ax1.xaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y))) 
ax1.yaxis.tick_right() 
ax1.yaxis.set_ticks_position('none')
plt.yticks([0, 1], ["In Person", "Online"])
ax1.set_title("Course format enrollment, by gender identity", alpha=0.8)


        
ax2 = fig.add_subplot(3, 1, 2)
ax2.barh([0, 1], dfStanding["Non-Seniors"], color='darkcyan', edgecolor='white', 
        height=barWidth)
ax2.barh([0, 1], dfStanding["Seniors"], left=dfStanding["Non-Seniors"], 
        color='powderblue', edgecolor='white', height=barWidth)  

#removing frame and ticks
for spine in plt.gca().spines.values(): spine.set_visible(False)
plt.tick_params(axis='x', labelbottom=False)
ax2.yaxis.tick_right()
ax2.yaxis.set_ticks_position('none') 
plt.yticks([0, 1], ["In Person", "Online"])

ax2.set_title("Course format enrollment, by class standing", alpha=0.8)

ax3 = fig.add_subplot(3,1,3)
ax3.barh([0, 1], dfESL["English Only"], color='darkcyan', edgecolor='white', height=barWidth)
ax3.barh([0, 1], dfESL["English and Another"], left=dfESL["English Only"], 
        color='cadetblue', edgecolor='white', height=barWidth)     
barLeft = np.add(dfESL["English Only"], dfESL["English and Another"]).tolist()
ax3.barh([0, 1], dfESL["Another Language"], left = barLeft,
        color='powderblue', edgecolor='white', height=barWidth)
#removing frame and ticks
for spine in plt.gca().spines.values(): spine.set_visible(False)
#plt.tick_params(bottom=False, left=False) 

ax3.xaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
ax3.yaxis.tick_right()
ax3.yaxis.set_ticks_position('none')
plt.yticks([0, 1], ["In Person", "Online"])  
ax3.set_title("Course format enrollment, by language spoken at home", alpha=0.8)


plt.tight_layout()#this cleans up padding in layout      
plt.show()


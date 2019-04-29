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


#set up data frames using demographic numbers

Online = {"Women":238, "Men":178, "Seniors":166, "Non-Seniors":251, 
          "English Only":192, "English and Another":108, "Another language":117}
inPerson = {"Women":316, "Men":320, "Seniors":91, "Non-Seniors":545, 
          "English Only":350, "English and Another":143, "Another language":143}

dfGender = pd.DataFrame([inPerson, Online], columns=["Men", "Women"], 
                        index=["In Person", "Online"])

dfStanding = pd.DataFrame([inPerson, Online], columns=["Non-Seniors", "Seniors"], 
                        index=["In Person", "Online"])

dfESL =  pd.DataFrame([inPerson, Online], columns=["English Only", 
                      "English and Another", "Another language"], 
                        index=["In Person", "Online"])

#a couple of tests of basic percent stacked barplots
#using https://python-graph-gallery.com/13-percent-stacked-barplot/ for reference

#Have to normalize bars by total.

#Testing gender distribution stacked bars:
barWidth = 0.85
#names
plt.bar([0, 1], dfGender["Women"], color='#b5ffb9', edgecolor='white', width=barWidth)
plt.bar([0,1], dfGender["Men"], bottom=dfGender["Women"], color='#f9bc86', edgecolor='white', width=barWidth)     
        
        
        
plt.show()
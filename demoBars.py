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
import matplotlib.font_manager 
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




#Testing gender distribution stacked bars:
barWidth = 0.85
color1 = 'darkcyan'#bar and formatting colors
color2 =  'cadetblue'
color3 = 'powderblue'

fig = plt.figure(figsize = (8, 8))
#rcParams['axes.titlepad'] = 20 



#Plot 1: Gender identity
ax1 = fig.add_subplot(3, 1, 1)
ax1.invert_yaxis()#otherwise, barplots go from lesser to greater y
ax1.set_facecolor('white')
ax1.barh([0, 1], dfGender["Men"], color='#008EAA', edgecolor='white', height=barWidth)
ax1.barh([0, 1], dfGender["Women"], left=dfGender["Men"], color='#00B5E2', 
         edgecolor='white', height=barWidth) 
#removing frame and ticks
for spine in plt.gca().spines.values(): spine.set_visible(False) 
plt.tick_params(axis='x', labelbottom=False)
#should make object oriented coding consistent here
ax1.xaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y))) 
ax1.yaxis.tick_right() 
ax1.yaxis.set_ticks_position('none')
ax1.xaxis.set_ticks_position('none')
plt.yticks([0, 1], ["In Person (n=636)", "Online (n=416)"])
ax1.set_title("Course format enrollment, by gender identity", alpha=0.8, pad=18)




 #Plot 2: Class Standing       
ax2 = fig.add_subplot(3, 1, 2)
ax2.invert_yaxis()
ax2.set_facecolor('white')
ax2.barh([0, 1], dfStanding["Non-Seniors"], color='#008EAA', edgecolor='white', 
        height=barWidth)
ax2.barh([0, 1], dfStanding["Seniors"], left=dfStanding["Non-Seniors"], 
        color='#00B5E2', edgecolor='white', height=barWidth)  

#removing frame and ticks
for spine in plt.gca().spines.values(): spine.set_visible(False)
plt.tick_params(axis='x', labelbottom=False)
ax2.yaxis.tick_right()
ax2.yaxis.set_ticks_position('none') 
ax2.xaxis.set_ticks_position('none')
plt.yticks([0, 1], ["In Person (n=636)", "Online (n=417)"])

ax2.set_title("Course format enrollment, by class standing", alpha=0.8, pad=18)



#Plot 3: Language
ax3 = fig.add_subplot(3,1,3)
ax3.invert_yaxis()
ax3.set_facecolor('white')
ax3.barh([0, 1], dfESL["English Only"], color='#5B7F95', edgecolor='white', height=barWidth)
ax3.barh([0, 1], dfESL["English and Another"], left=dfESL["English Only"], 
        color='#008EAA', edgecolor='white', height=barWidth)     
barLeft = np.add(dfESL["English Only"], dfESL["English and Another"]).tolist()
ax3.barh([0, 1], dfESL["Another Language"], left = barLeft,
        color='#00B5E2', edgecolor='white', height=barWidth)
#removing frame and ticks
for spine in plt.gca().spines.values(): spine.set_visible(False)
plt.tick_params(bottom=False, left=False) 

#ax3.xaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
ax3.yaxis.tick_right()
ax3.yaxis.set_ticks_position('none')
ax3.set_xticklabels([])
ax3.xaxis.set_ticks_position('none')
plt.yticks([0, 1], ["In Person (n=636)", "Online (n=417)"])  
ax3.set_title("Course format enrollment, by language spoken at home", alpha=0.8, pad=18)


#label for ax1 gender
i = 0
rects = ax1.patches
labels = ["50.3%", "42.8%", "49.7%", "57.2%"]


for rect in rects:
    # Get X and Y placement of label from rect.
    x_value = rect.get_x()
    y_value = rect.get_y() +(rect.get_height()/2)
      # Number of points between bar and label. Change to your liking.
    space = 5
    # Vertical alignment for positive values
    ha = 'left'
    
    label = labels[i]
    i=i+1
   
    ax1.annotate(
        label,                      # Use `label` as label
        (x_value, y_value),         # Place label at end of the bar
        xytext=(space, 0),          # Horizontally shift label by `space`
        textcoords="offset points", # Interpret `xytext` as offset in points
        va='center',                # Vertically center label
        ha=ha,# Horizontally align label differently for
        color='white', 
        #fontweight='bold',
        fontsize=14)
  
#Men title on top of rectangle
rect=rects[0]

x_value = (rect.get_x()+rect.get_width())/2
y_value = rect.get_y()-.1

ax1.annotate(
        "Men",                      # Use `label` as label
        (x_value, y_value),         # Place label at end of the bar
        xytext=(space, 0),          # Horizontally shift label by `space`
        textcoords="offset points", # Interpret `xytext` as offset in points
        va='center',                # Vertically center label
        ha="center",# Horizontally align label differently for
        color='#008EAA', 
        #fontweight='bold',
        fontsize=13)

# women title on top of respective rectangle
rect=rects[2]

x_value = rect.get_x()+(rect.get_width())/2
y_value = rect.get_y()-.1

ax1.annotate(
        "Women",                      # Use `label` as label
        (x_value, y_value),         # Place label at end of the bar
        xytext=(space, 0),          # Horizontally shift label by `space`
        textcoords="offset points", # Interpret `xytext` as offset in points
        va='center',                # Vertically center label
        ha="center",
        color='#00B5E2', 
        #fontweight='bold',
        fontsize=13)





              
#label for ax2 class standing
i = 0
rects = ax2.patches
labels = ["85.7%", "60.2%",
          "14.3% ", "39.8%"]



for rect in rects:
    # Get X and Y placement of label from rect.
    x_value = rect.get_x()
    y_value = rect.get_y() +(rect.get_height()/2)
      # Number of points between bar and label. Change to your liking.
    space = 5
    # Vertical alignment for positive values
    ha = 'left'
    
    label = labels[i]
   
   
    if i==2:
        ax2.annotate(
        label,                      # Use `label` as label
        (x_value, y_value),         # Place label at end of the bar
        xytext=(2, 0),          # Horizontally shift label by `space`
        textcoords="offset points", # Interpret `xytext` as offset in points
        va='center',                # Vertically center label
        ha=ha, 
        color='white', 
        #fontweight='bold', 
        fontsize=12) 
    else:
        ax2.annotate(
        label,                      # Use `label` as label
        (x_value, y_value),         # Place label at end of the bar
        xytext=(space, 0),          # Horizontally shift label by `space`
        textcoords="offset points", # Interpret `xytext` as offset in points
        va='center',                # Vertically center label
        ha=ha, 
        color='white', 
        #fontweight='bold', 
        fontsize=14)
        
    i=i+1
    
#top titles
    
rect=rects[0]

x_value = (rect.get_x()+rect.get_width())/2
y_value = rect.get_y()-.1    

ax2.annotate(
        "Underclassmen",                      # Use `label` as label
        (x_value, y_value),         # Place label at end of the bar
        xytext=(space, 0),          # Horizontally shift label by `space`
        textcoords="offset points", # Interpret `xytext` as offset in points
        va='center',                # Vertically center label
        ha="center",# Horizontally align label differently for
        color='#008EAA', 
        #fontweight='bold',
        fontsize=13)

# women title on top of respective rectangle
rect=rects[2]

x_value = rect.get_x()+(rect.get_width())/2
y_value = rect.get_y()-.1

ax2.annotate(
        "Seniors",                      # Use `label` as label
        (x_value, y_value),         # Place label at end of the bar
        xytext=(space, 0),          # Horizontally shift label by `space`
        textcoords="offset points", # Interpret `xytext` as offset in points
        va='center',                # Vertically center label
        ha="center",
        color='#00B5E2', 
        #fontweight='bold',
        fontsize=13)

        

#label for ax3 language
i = 0
rects = ax3.patches
labels = ["55.0%", "46.0%", 
          "22.5%", "25.9%", 
          "22.5%", "28.1%"]



for rect in rects:
    # Get X and Y placement of label from rect.
    x_value = rect.get_x()
    y_value = rect.get_y() +(rect.get_height()/2)
      # Number of points between bar and label. Change to your liking.
    space = 5
    # Vertical alignment for positive values
    ha = 'left'
    
    label = labels[i]
    
    if i <=1:
        ax3.annotate(
        label,                      # Use `label` as label
        (x_value, y_value),         # Place label at end of the bar
        xytext=(space, 0),          # Horizontally shift label by `space`
        textcoords="offset points", # Interpret `xytext` as offset in points
        va='center',                # Vertically center label
        ha=ha,         
        color='white', 
        #fontweight='bold', 
        fontsize=14) 
    else:
        ax3.annotate(
        label,                      # Use `label` as label
        (x_value, y_value),         # Place label at end of the bar
        xytext=(space, 0),          # Horizontally shift label by `space`
        textcoords="offset points", # Interpret `xytext` as offset in points
        va='center',                # Vertically center label
        ha=ha,         
        color='white', 
        #fontweight='bold', 
        fontsize=12) 
     
    i=i+1

#top titles
    
rect=rects[0]

x_value = (rect.get_x()+rects[1].get_width())/2
y_value = rect.get_y()-.1    

ax3.annotate(
        "English Only",                      # Use `label` as label
        (x_value, y_value),         # Place label at end of the bar
        xytext=(space, 0),          # Horizontally shift label by `space`
        textcoords="offset points", # Interpret `xytext` as offset in points
        va='center',                # Vertically center label
        ha="center",# Horizontally align label differently for
        color='#5B7F95', 
        #fontweight='bold',
        fontsize=13)

# English and Aother title on top of respective rectangle
rect=rects[2]

x_value = rects[3].get_x()+rects[3].get_width()/2
y_value = rect.get_y()-.1

ax3.annotate(
        "English & Another",                      # Use `label` as label
        (x_value, y_value),         # Place label at end of the bar
        xytext=(space, 0),          # Horizontally shift label by `space`
        textcoords="offset points", # Interpret `xytext` as offset in points
        va='center',                # Vertically center label
        ha="center",
        color='#008EAA', 
        #fontweight='bold',
        fontsize=13)   

rect=rects[4]

x_value = rect.get_x()+(rect.get_width())/2
y_value = rect.get_y()-.1

ax3.annotate(
        "Another Language",                      # Use `label` as label
        (x_value, y_value),         # Place label at end of the bar
        xytext=(space, 0),          # Horizontally shift label by `space`
        textcoords="offset points", # Interpret `xytext` as offset in points
        va='center',                # Vertically center label
        ha="center",
        color='#00B5E2', 
        #fontweight='bold',
        fontsize=12) 

#plt.tight_layout()#this cleans up padding in layout     
plt.subplots_adjust(hspace = 0.8, top = .8) 
plt.show()


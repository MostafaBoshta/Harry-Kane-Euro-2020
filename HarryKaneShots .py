# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 18:56:51 2022

@author: mosta
"""

import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsbombpy import sb
#from mplsoccer import Sbopen
import pandas as pd
#parser = Sbopen()
euro = sb.matches(competition_id = 55 , season_id=43)
Englandmatches = []
for i,match in euro.iterrows():
    if (match['home_team'] == 'England' or match['away_team'] == 'England'):
        Englandmatches.append(match['match_id'])


#chiesa_Passes = 0
#chiesa_BallReceipt = 0
#chiesa_Carry = 0
#chiesa_Pressure = 0
#chiesa_BallRecovery = 0

pitchLengthX = 120
pitchWidthY = 80
from FCPython import createPitch
(fig,ax) = createPitch(pitchLengthX , pitchWidthY , 'yards' , 'black')
goals = 0
shots = 0
#print(Englandmatches)
#example = sb.events(match_id = Englandmatches[0])        
for England_match in Englandmatches:
    for j,event in sb.events(match_id=England_match).iterrows():
        if event.player == 'Harry Kane' and event.type == 'Shot':
            #circleSize=np.sqrt(event['shot_statsbomb_xg'])*12
            x = event.location[0]
            y = event.location[1]
            goal = event['shot_outcome'] == 'Goal'
            shots +=1
            if goal:
                    shotCircle=plt.Circle((x,pitchWidthY-y),2,color="red")
                    shotCircle.set_alpha(.7)
                    goals +=1
            else:
                    shotCircle=plt.Circle((x,pitchWidthY-y),1,color="red")     
                    shotCircle.set_alpha(.2)
                   
            ax.add_patch(shotCircle) 
            
plt.text(75,75,'Harry Kane shots') 
plt.text(75 , 70 , 'Total Shots: ' + str(shots))
plt.text(75 , 65 , 'Goals: ' + str(goals))
plt.text(75 , 60 , 'Conversion Rate: ' + str(round((goals/shots)*100,2)) + '%' )     
fig.set_size_inches(10, 7)
fig.savefig('Harry Kane', dpi=300) 
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 00:45:53 2022

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


pitchLengthX = 120
pitchWidthY = 80
from FCPython import createPitch
(fig,ax) = createPitch(pitchLengthX , pitchWidthY , 'yards' , 'black')
assists = 0
passe = 0
#print(Englandmatches)
example = sb.events(match_id = Englandmatches[0])        
for England_match in Englandmatches:
        for j,event in sb.events(match_id=England_match).iterrows():
        
        
    
            if event.player == 'Harry Kane' and event.type == 'Pass':
            #circleSize=np.sqrt(event['shot_statsbomb_xg'])*12
                passe +=1
            
                x = event['location'][0]
                y = event['location'][1]
            
            
                PassCircle=plt.Circle((x,pitchWidthY-y),2,color="blue")  
                PassCircle.set_alpha(.2)
                ax.add_patch(PassCircle)
                z = event['pass_end_location'][0]-x
                q = event['pass_end_location'][1]-y
                PassArrow = plt.Arrow(x, pitchWidthY-y, z, q, width=2  , color = 'blue' )
                ax.add_patch(PassArrow)
           
plt.text(5,75,'Harry Kane Passes') 
plt.text(5 , 70 , 'Total Passes: ' + str(passe))
#plt.text(75 , 65 , 'Goals: ' + str(goals))
#plt.text(75 , 60 , 'Conversion Rate: ' + str(round((goals/shots)*100,2)) + '%' )     
fig.set_size_inches(10, 7)

fig.savefig('Harry Kane Passes', dpi=300) 
plt.show()
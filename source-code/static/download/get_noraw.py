import numpy as np
import pandas as pd
import sys
import json
import time
from telnetlib import Telnet

# Initializing the arrays required to store the data.
attention_values = np.array([])
meditation_values = np.array([])
delta_values = np.array([])
theta_values = np.array([])
lowAlpha_values = np.array([])
highAlpha_values = np.array([])
lowBeta_values = np.array([])
highBeta_values = np.array([])
lowGamma_values = np.array([])
highGamma_values = np.array([])
blinkStrength_values = np.array([])
time_array = np.array([])

tn=Telnet('127.0.0.1',13854)

start=time.time()

i=0
#st = '{"enableRawOutput": true, "format": "Json"}'
#tn.write(st.encode())
tn.write(b'{"enableRawOutput": false, "format": "Json"}')


outfile="null"
if len(sys.argv)>1:
    outfile=sys.argv[len(sys.argv)-1]
    outfptr=open(outfile,'w')

eSenseDict={'attention':0, 'meditation':0}
waveDict={'lowGamma':0, 'highGamma':0, 'highAlpha':0, 'delta':0, 'highBeta':0, 'lowAlpha':0, 'lowBeta':0, 'theta':0}
signalLevel=0
outfptr.write("timediff, signalLevel, blinkStrength, attention, meditation, lowGamma, highGamma, highAlpha, delta, highBeta, lowAlpha, lowBeta, theta\n")

while time.time() - start < 30:
    blinkStrength=0
    line=tn.read_until(b"\r")
    dataline = line.decode()
    if len(dataline) > 20:	
        timediff=time.time()-start
        #print(json.loads(dataline))
        dict=json.loads(dataline)
        if "poorSignalLevel" in dict:
            signalLevel=dict['poorSignalLevel']
        if "blinkStrength" in dict:
            blinkStrength=dict['blinkStrength']
        if "eegPower" in dict:
            waveDict=dict['eegPower']
            eSenseDict=dict['eSense']
        outputstr=str(timediff)+ ", "+ str(signalLevel)+", "+str(blinkStrength)+", " + str(eSenseDict['attention']) + ", " + str(eSenseDict['meditation']) + ", "+str(waveDict['lowGamma'])+", " + str(waveDict['highGamma'])+", "+ str(waveDict['highAlpha'])+", "+str(waveDict['delta'])+", "+ str(waveDict['highBeta'])+", "+str(waveDict['lowAlpha'])+", "+str(waveDict['lowBeta'])+ ", "+str(waveDict['theta'])
        time_array = np.append(time_array, [timediff])
        blinkStrength_values = np.append(blinkStrength_values, [blinkStrength])
        lowGamma_values = np.append(lowGamma_values, [waveDict['lowGamma']])
        highGamma_values = np.append(highGamma_values, [waveDict['highGamma']])
        highAlpha_values = np.append(highAlpha_values, [waveDict['highAlpha']])
        delta_values = np.append(delta_values, [waveDict['delta']])
        lowBeta_values = np.append(lowBeta_values, [waveDict['lowBeta']])
        highBeta_values = np.append(highBeta_values, [waveDict['highBeta']])
        theta_values = np.append(theta_values, [waveDict['theta']])
        lowAlpha_values = np.append(lowAlpha_values, [waveDict['lowAlpha']])
        attention_values = np.append(attention_values, [eSenseDict['attention']])
        meditation_values = np.append(meditation_values, [eSenseDict['meditation']])
        print (outputstr)
        if outfile!="null":	
            outfptr.write(outputstr+"\n")		

tn.close()
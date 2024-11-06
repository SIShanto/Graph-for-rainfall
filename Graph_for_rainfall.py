import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import matplotlib.dates as mdates
from matplotlib import style

#using dpi for better resolution of graph
plt.rcParams['savefig.dpi']= 350
df= pd.read_excel('2004 to 2007 comple.xlsx')

x= df["DATE"]
y= df["RAINFALL "]

# for bar graph of rainfall
style.use('ggplot')
fig,ax= plt.subplots()

ax.bar(x,y,color="blue",label='Rainfall (mm)')
ax.set(ylim=(None,200))
ax.grid()
ax.invert_yaxis()

ax.set_ylabel("Rainfall (mm)", rotation=90, labelpad=20, fontsize=20, color='black', fontweight='bold')
plt.yticks(fontsize=17, color='black',fontweight='bold')
plt.xlabel('Date', fontsize= 20, labelpad=11, color='black', fontweight='bold')
plt.xticks(fontsize=16,fontweight='bold')

ax.xaxis.set_major_formatter(mdates.DateFormatter('%b,%Y'))
ax.tick_params(bottom=True,labelbottom=True)
ax.tick_params(axis='x', labelrotation=21, color='black', labelcolor='black')
plt.legend(frameon=False,loc=(577/1453,108/200),fontsize=15)
# plt.gca().set_facecolor('white')

# for observed graph
b=df["FLOW-OBSERVED (M3/S)"]
bx=ax.twinx()
bx.plot(x,b, color='green',label='Observed-Flow (m\u00b3/s)')

for line in ['left','bottom','top','right']:  # for making every side line visible
    bx.spines[line].set_color('black')
    
bx.set(ylim=(None,22000))
# bx.set_yticks([])
plt.grid(False)

# for flow graph
c=df['FLOW (M3/S)']
# cx=bx.twinx()
plt.plot(x,c,'--',color='red', label='Simulated-Flow (m\u00b3/s)')
plt.ylim((None,22000))

plt.yticks(fontsize=17, color='black',fontweight='bold')
plt.ylabel("Flow (m\u00b3/s)", rotation=90, labelpad=22, fontsize=20, color='black',fontweight='bold')

plt.grid(False)
plt.legend(frameon=False, loc='center',fontsize=15)
plt.show()

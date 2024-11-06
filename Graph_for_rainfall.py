import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import matplotlib.dates as mdates
from matplotlib import style

plt.rcParams['savefig.dpi']= 800

df= pd.read_excel('2004 to 2007 comple.xlsx')

x= df["DATE"]
y= df["RAINFALL "]

# for bar graph of rainfall

style.use('ggplot')
fig,ax= plt.subplots()

ax.bar(x,y,color="blue")
ax.set(ylim=(None,200))
ax.grid(False)
ax.invert_yaxis()
ax.set_ylabel("RAINFALL", rotation=90, labelpad=20, fontsize=15, color='black')

plt.yticks(fontsize=13, color='black')
plt.xlabel('DATE', fontsize= 15, labelpad=15, color='black')
plt.xticks(fontsize=11, color='black')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b,%Y'))
ax.tick_params(top=False, labeltop=False, bottom=True,labelbottom=True)
ax.tick_params(axis='x', labelrotation=20, color='black', labelcolor='black')
# plt.gca().set_facecolor('white')

# for flow graph
b=df["FLOW (M3/S)"]
bx=ax.twinx()
bx.plot(x,b, color='green',label='FLOW (m3/s)')

for line in ['left','bottom','top','right']:  # for making every side line visible
    bx.spines[line].set_color('black')
  
bx.set(ylim=(None,22000))
# bx.set_yticks([])
plt.grid(False)

# for observed flow graph
c=df['FLOW-OBSERVED (M3/S)']
# cx=bx.twinx()
plt.plot(x,c,'--',color='red', label='FLOW-OBSERVED (m3/s)')
plt.ylim((None,22000))
plt.yticks(fontsize=12, color='black')
plt.ylabel("FLOW (m3/s)", rotation=90, labelpad=25, fontsize=15, color='black')
plt.grid(False)

# set the legends and plot the graph
plt.legend(loc="center", fontsize=12)
plt.show()

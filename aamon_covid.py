# -*- coding: utf-8 -*-
"""aamon_covid.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OJEjjS3TnrGXyM3mkOclfTRdo1uwNqrn
"""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
plt.style.use('classic')
# %matplotlib inline
import seaborn as sns
import pandas as pd
import numpy as np
data = pd.read_csv("https://raw.githubusercontent.com/kalyaniuniversity/COVID-19-Datasets/master/India%20Statewise%20Confirmed%20Cases/COVID19_INDIA_STATEWISE_TIME_SERIES_CONFIRMED.csv")
data

total_infected=data.iloc[:37,-1:].values.sum()
print("Total infected number of people till",data.columns[-1], "are" , total_infected)

i=0
sum=0
# while(i<=37):
#  sum=sum+(data.iloc[[i],[-1]].values.sum() - data.iloc[[i],[-2]].values.sum())
#  i=i+1 
# print(sum) 
last_day=data.iloc[:37,-1:].values.sum() - data.iloc[:37,-2:-1].values.sum()
print("Last day's number of new cases are:",last_day)

i=0
while(i<37):
 if(data.iloc[[i],[-1]].values == data.iloc[:37,-1:].values.max()):
  print("Region with Highest Infection:",data.iloc[[i],[0]].values.sum(),data.iloc[:37,-1:].values.max())
  print("Last day's number of new cases are:",data.iloc[[i],[-1]].values.sum() - data.iloc[[i],[-2]].values.sum())
 i=i+1

i=7
sub=0
max=0
last_col=data.shape[1] - 2
while(i<=last_col):
  sub=data.iloc[[-1],[i+1]].values.sum()-data.iloc[[-1],[i]].values.sum()
  if max<sub:
    max=sub
  i=i+1
i=7
while(i<=last_col):
  if(data.iloc[[-1],[i+1]].values.sum()-data.iloc[[-1],[i]].values.sum()==max):
    print("India's Highest Infection Spike in 1 Day:",max,"between",data.columns[i],"and",data.columns[i+1])
  i=i+1

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data2 = pd.read_csv("https://raw.githubusercontent.com/kalyaniuniversity/COVID-19-Datasets/master/India%20Statewise%20Recovery%20Cases/COVID19_INDIA_STATEWISE_TIME_SERIES_RECOVERY.csv")
data2

plt.figure(figsize=(26,8))
i=7
last_col=data.shape[1] - 2
sns.lineplot(data=data.iloc[-1,7::30].values,label="Total Infected")
sns.lineplot(data=data2.iloc[-1,7::30],label="Total Recovered")

total_recovered=data2.iloc[:37,-1:].values.sum()
print("Total recovered number of people till",data2.columns[-1], "are" , total_recovered)

i=0
sum=0
while(i<=37):
#  sum=sum+(data2.iloc[[i],[-1]].values.sum() - data2.iloc[[i],[-2]].values.sum())
  i=i+1 
print(sum)
last_day=data2.iloc[:37,-1:].values.sum() - data2.iloc[:37,-2:-1].values.sum()
print("Last day's number of recovered cases are:",last_day)

i=0
while(i<=37):
 if(data2.iloc[[i],[-1]].values == data2.iloc[:37,-1:].values.max()):
  print("Region with Highest Recovered Cases:",data2.iloc[[i],[0]].values.sum(),data2.iloc[:37,-1:].values.max())
  print("Last day's number of new Recovered cases are:",data2.iloc[[i],[-1]].values.sum() - data2.iloc[[i],[-2]].values.sum())
 i=i+1

i=7
sub=0
max=0
last_col=data.shape[1] - 2
while(i<=last_col):
  sub=data2.iloc[[-1],[i+1]].values.sum()-data2.iloc[[-1],[i]].values.sum()
  if max<sub:
    max=sub
  i=i+1
i=7
while(i<=last_col):
  if(data2.iloc[[-1],[i+1]].values.sum()-data2.iloc[[-1],[i]].values.sum()==max):
    print("India's Highest Recovery Spike in 1 Day:",max,"between",data2.columns[i],"and",data2.columns[i+1])
  i=i+1

i=1
#data.iloc[,0]
last_col=data.shape[1] - 2
last_col
#sns.set_style("darkgrid")
plt.figure(figsize=(80,30))
#data.iloc[:,last_col]
#data.iloc[:,0]
#while(i<36):

sns.barplot(x=data.iloc[:-1,0], y=data.iloc[::,last_col],order=data.sort_values("10/22/2021",ascending = False).iloc[:-1,0]);
#  i=i+1

#sns.set_theme(style="whitegrid")
#sns.barplot(data=data.iloc[:,-1])

#data.iloc[0:37,0]
#data.iloc[0:37,-1]
#while(i<37):
#  print("Total infected of state",data.iloc[i,0], "is", data.iloc[i,-1])
 # i=i+1

sub=0
max=0
i=0
last_col=data.shape[1] - 2
while(i<36):
  print(data.iloc[i,0],"----->",data.iloc[[i],[-4]].values.sum()-data.iloc[[i],[-5]].values.sum())
  sub=sub+data.iloc[[i],[-4]].values.sum()-data.iloc[[i],[-5]].values.sum()
  i=i+1
print(data.iloc[i,0],"------>",sub)
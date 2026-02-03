import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv("Sleep_Deprivation_Analysis\sleep_deprevation.csv" ,
                usecols = ['Sleep_Hours' , 'PVT_Reaction_Time'])

x = df['Sleep_Hours']
y = df['PVT_Reaction_Time']
plt.xlabel('Sleep Hours')
plt.ylabel('PVT Reaction Time')
plt.scatter(x,y)
plt.show()
"""plt.hist(df['Sleep_Hours'])

plt.show()"""
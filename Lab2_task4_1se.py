import pandas as pd
import random as rd
import seaborn as se
import matplotlib.pyplot as plt


pd_titanic=pd.read_csv("titanic.csv")

pd_titanic_clean=pd_titanic.dropna(subset=['Survived',  'Sex'])

se.relplot(data=pd_titanic_clean,x="Fare",y="Age",hue="Survived",col="Sex",height=5,aspect=1.2,palette="Set1")
plt.show()
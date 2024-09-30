import pandas as pd
import random as rd
import seaborn as se
import matplotlib.pyplot as plt


pd_titanic=pd.read_csv("titanic.csv")

se.barplot(data=pd_titanic,x="Pclass",y="Survived",hue="Sex")
plt.show()
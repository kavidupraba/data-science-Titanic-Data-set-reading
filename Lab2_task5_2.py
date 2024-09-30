import pandas as pd
import seaborn as se
import matplotlib.pyplot as pl

pd_titanic=pd.read_csv("titanic.csv")

age_ajusted=pd_titanic[pd_titanic["Age"]>=14]

se.barplot(data=age_ajusted,x="Pclass",hue="Sex",y="Survived")
pl.show()

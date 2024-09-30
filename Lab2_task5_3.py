import pandas as pd
import seaborn as se
import matplotlib.pyplot as pl

pd_titanic=pd.read_csv("titanic.csv")

age_ajust=pd_titanic[pd_titanic["Age"]<=14]

se.countplot(data=age_ajust,x="Pclass",hue="Sex")
#se.barplot(data=pd_titanic,x="Pclass",y="Fare",hue="Sex")
#se.countplot(data=pd_titanic,x="Pclass",hue="Sex")
pl.show()
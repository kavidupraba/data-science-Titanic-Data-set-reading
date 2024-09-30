import pandas as pd
import seaborn as se
import matplotlib.pyplot as pl

pd_titanic=pd.read_csv("titanic.csv")
pd_titanic_nona=pd_titanic.dropna(subset=["Cabin"]).copy()

pd_titanic_nona.loc[:,"Level"]=pd_titanic_nona["Cabin"].str[0]

Pcl_adjusted=pd_titanic_nona[pd_titanic_nona["Pclass"]==1]

se.barplot(data=Pcl_adjusted,x="Level",y="Fare",hue="Pclass")
pl.show()

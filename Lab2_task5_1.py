import pandas as pd
import seaborn as se
import matplotlib.pyplot as pl


pd_titanic=pd.read_csv("titanic.csv")
age_group=pd_titanic[pd_titanic["Age"]<14]

se.barplot(x="Pclass",y="Survived",hue="Sex",data=age_group)
pl.show()
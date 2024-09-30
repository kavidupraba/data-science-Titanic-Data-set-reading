import pandas as pd
import seaborn as se
import matplotlib.pyplot as pl

pd_titanic=pd.read_csv("titanic.csv")
pd_titanic_nona=pd_titanic.dropna(subset="Cabin").copy()

pd_titanic_nona.loc[:,"Level"]=pd_titanic_nona["Cabin"].str[0]

Pcl_adjusted=pd_titanic_nona[pd_titanic_nona["Pclass"]==1]

gendercount=Pcl_adjusted.groupby("Level")["Sex"].value_counts().unstack(fill_value=0)

genderratio=gendercount.div(gendercount.sum(axis=1),axis=0)

genderratio.reset_index(inplace=True)

genderratio.plot(x="Level",kind="bar",stacked=False)
pl.ylabel("Proportion")
pl.title("Male and Female Gender ratio")
pl.show()
'''
axis=0 operates along rows (column-wise). So it processes each column one by one.
axis=1 operates along columns (row-wise). So it processes each row one by one, combining
'''
#print(gendercount)
#print(genderratio)
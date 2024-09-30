import pandas as pd
import seaborn as se
import matplotlib.pyplot as pl

pd_titanic=pd.read_csv("titanic.csv")
pd_titanic_nona=pd_titanic.dropna(subset=["Cabin"]).copy()
#pd_titanic_nona=pd_titanic.dropna(subset=["Cabin"])
pd_titanic_nona.loc[:,"Level"]=pd_titanic_nona["Cabin"].str[0]
#pd_titanic_nona["Level"]=pd_titanic_nona["Cabin"].str[0]

print(pd_titanic_nona[["Level","Cabin"]])
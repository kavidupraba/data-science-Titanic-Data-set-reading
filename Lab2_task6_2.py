import pandas as pd
import seaborn as se
import matplotlib.pyplot as pl

pd_titanic=pd.read_csv("titanic.csv")

#answer 1
#df_titanic_nona=pd_titanic["Cabin"].dropna()
#answer 2
df_titanic_nona=pd_titanic.dropna(subset=["Cabin"])

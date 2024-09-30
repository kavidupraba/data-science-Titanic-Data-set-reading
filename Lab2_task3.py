import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df_titanic=pd.read_csv("titanic.csv")
#print(df_titanic.to_string())#read the csv file
df_titanic["Age_imp_mean"]=df_titanic["Age"]
#print(df_titanic.isnull().sum())
df_titanic["Age_imp_mean"]=df_titanic["Age_imp_mean"].fillna(value=df_titanic["Age"].mean())
#print(df_titanic.isnull().sum())
df_titanic["Age_imp_ffill"]=df_titanic["Age"]
df_titanic["Age_imp_ffill"]=df_titanic["Age_imp_ffill"].ffill()
#print(df_titanic.isnull().sum())
print(df_titanic)
klist={"Age_imp_mean":[],"Age_imp_ffill":[],"Age":[]}
klist["Age_imp_mean"]=df_titanic["Age_imp_mean"]
klist["Age_imp_ffill"]=df_titanic["Age_imp_ffill"]
klist["Age"]=df_titanic["Age"].dropna()

df_Klist=pd.DataFrame(data=klist)
#df_Klist.dropna(inplace=True)
"""
sns.histplot(df_Klist["Age_imp_mean"], kde=False, bins=40, label="Age_imp_mean", color="blue")
sns.histplot(df_Klist["Age_imp_ffill"], kde=False, bins=40, label="Age_imp_ffill", color="green")
sns.histplot(df_Klist["Age"].dropna(), kde=False, bins=40, label="Age", color="red")
plt.legend()
"""
sns.histplot(data=df_Klist,kde=False,bins=40,alpha=0.6)
plt.xlabel("Age")
plt.show()
#sns.histplot(data=df_Klist.dropna(),kde=False,bins=40)
#sns.histplot(data=df_Klist,kde=False,bins=40)
sns.boxplot(df_Klist)
plt.xlabel("Age")
plt.show()



'''
df_titanic["Age_imp_mean"]=df_titanic["Age"].fillna(value=df_titanic["Age"].mean())
print(df_titanic.to_string())
'''

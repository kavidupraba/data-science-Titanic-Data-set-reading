import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df_titanic=pd.read_csv("titanic.csv")
print(df_titanic.to_string())#read the csv file
#print("*******************************")
df_titanic_null=df_titanic.isnull()
print(df_titanic_null.to_string())#print the data in csv file
#print("*******************************")
df_titanic_null_sum=df_titanic_null.sum()
df_titanic_info=df_titanic.info()
print(df_titanic_info)
print(df_titanic_null_sum)#print the null sum
#plt.show()
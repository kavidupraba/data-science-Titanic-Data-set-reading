import pandas as pd
import seaborn as se
import matplotlib.pyplot as pl


pd_titanic=pd.read_csv("titanic.csv")

Presentage_count=pd_titanic.groupby("Pclass")["Cabin"].apply(lambda x:x.isnull().mean()*100)

for i,j in zip(Presentage_count,[1,2,3]):
    print(f"Pclass{j}:  {i:.3f}%")

print(Presentage_count)
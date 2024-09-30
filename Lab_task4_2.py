import pandas as pd
import random as rd
import seaborn as se
import matplotlib.pyplot as plt


pd_titanic=pd.read_csv("titanic.csv")
titanic_dic={"Pclass":pd_titanic["Pclass"],"Fare":pd_titanic["Fare"],"Sex":pd_titanic["Sex"]}


titanic_dic_cp=pd.DataFrame(titanic_dic)

se.boxplot(x="Pclass",y="Fare",hue="Sex",data=titanic_dic_cp)
plt.show()
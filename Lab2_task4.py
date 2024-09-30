import pandas as pd
import random as rd
import seaborn as se
import matplotlib.pyplot as plt


pd_titanic=pd.read_csv("titanic.csv")

pd_titanic_clean=pd_titanic.dropna(subset=['Survived',  'Sex'])
colors=pd_titanic_clean["Survived"].map({0:'red',1:'green'})


fig, axes=plt.subplots(1,2,figsize=(6.4,4.8),sharey=True)

pd_titanic_clean[pd_titanic_clean["Sex"]=="female"].plot.scatter(
    x="Fare",
    y="Age",
    c=colors[pd_titanic_clean["Sex"]=="female"],
    ax=axes[0],
    title="Female"
)

pd_titanic_clean[pd_titanic_clean["Sex"]=="male"].plot.scatter(
    x="Fare",
    y="Age",
    c=colors[pd_titanic_clean["Sex"]=="male"],
    ax=axes[1],
    title="Male"
)
fig.suptitle("Scatter chart of Titanic survival rate fare aginst age and colord the survival points and chart is separated from sex")
plt.show()
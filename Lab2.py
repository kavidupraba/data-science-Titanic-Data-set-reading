
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np



df_random=pd.DataFrame(data=np.random.normal(size=1000),columns=["number"]).reset_index()

sns.lineplot(x="index",y="number",data=df_random)
plt.show()



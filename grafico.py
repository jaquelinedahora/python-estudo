import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/ourcodingclub/CC-python-pandas-matplotlib/master/scottish_hills.csv"

df = pd.read_csv(url,delimiter=",")

colunas = ["Height", "Latitude"]

#print(df.plot(kind="bar"))
#df[colunas].plot(kind="scatter")
plt.bar(df["Height"],df["Latitude"])

plt.xlabel("Altura (m)", fontsize=20)
plt.ylabel("Latitude", fontsize=20)

plt.show()
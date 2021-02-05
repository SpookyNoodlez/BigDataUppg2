import pandas as pd


wine = pd.read_csv("wine.csv")

best = wine[wine.points == 100]

print(best)

#Här är det bästa vinet man kan köpa
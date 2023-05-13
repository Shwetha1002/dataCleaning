import pandas as pd
import csv 
df = pd.read_csv("mergeddata.csv")
print(df.columns)
del df["Luminosity"]
print(df.shape)
print(df.columns)
df.to_csv("Newmerged.csv")

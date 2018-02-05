import pandas as pd
from pandas import DataFrame
import numpy as np
from sklearn.preprocessing import OneHotEncoder
df = pd.read_csv('wchi_180117_recover2.csv', encoding='CP949')
print(df.isnull().sum())

#print(df["시군구"], df["요일"])
dummy=pd.get_dummies(df["시군구"], prefix="시군구")
print(dummy)

dummy2 = pd.get_dummies(df["요일"], prefix="요일")
print(dummy2)

df2 = pd.concat([df, dummy], axis=1)
print(df2)

df3 = pd.concat([df2, dummy2], axis=1)
print(df3)

df3.to_csv("wchi_180131.csv", encoding="CP949")
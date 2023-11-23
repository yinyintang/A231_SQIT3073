import os

os.system('cls')


import pandas as pd
a=["saya","suka","makan"]
b=pd.Series(a,index=["word1","word2","word3"])
print(b)
print(b["word2"])

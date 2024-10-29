import pandas as pd

#Importing the filtered csv files as data frames
df_bacillales = pd.read_csv("filtered_bacillales.csv")
print(df_bacillales.shape)

df_enterobacterales = pd.read_csv("filtered_enterobacterales.csv")
print(df_enterobacterales.shape)
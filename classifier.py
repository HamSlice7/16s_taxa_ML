import pandas as pd

#Importing the filtered csv files as data frames
df_bacillales = pd.read_csv("filtered_bacillales.csv")
print(df_bacillales.shape)

df_enterobacterales = pd.read_csv("filtered_enterobacterales.csv")
print(df_enterobacterales.shape)

#Balance the two data sets by randomly sampling 544 rows from df_bacillales
df_bacillales = df_bacillales.sample(n=544, random_state=25).reset_index(drop=True)
print(df_bacillales.shape)
print(df_bacillales.head())

#Add binary labels for gram positive and gram negative
df_bacillales["Label"] = 1
df_enterobacterales["Label"] = 0
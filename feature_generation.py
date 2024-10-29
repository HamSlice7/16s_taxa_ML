import pandas as pd
import k_mer

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

#Combine the df_bacillales and the df_enterobacterales data sets
df_combined = pd.concat([df_bacillales, df_enterobacterales]).reset_index(drop=True)
print(df_combined.shape)

#Generate K-mer of length two features

kmer_2 = k_mer.get_kmers(2)

for index,row in df_combined.iterrows():
    for kmer in kmer_2:
        print(f"Sequence: {index} {kmer} count :{row["Nucleotide Sequence"].count(kmer)}")
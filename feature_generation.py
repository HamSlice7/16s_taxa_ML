import pandas as pd
import k_mer
import numpy as np
#Importing the filtered csv files as data frames
df_bacillales = pd.read_csv("filtered_bacillales.csv")


df_enterobacterales = pd.read_csv("filtered_enterobacterales.csv")


#Balance the two data sets by randomly sampling 544 rows from df_bacillales
df_bacillales = df_bacillales.sample(n=544, random_state=25).reset_index(drop=True)

#Add binary labels for gram positive and gram negative
df_bacillales["Label"] = 1
df_enterobacterales["Label"] = 0

#Combine the df_bacillales and the df_enterobacterales data sets
df_combined = pd.concat([df_bacillales, df_enterobacterales]).reset_index(drop=True)


#Generate K-mer of length two features

kmer_2 = k_mer.get_kmers(2)


#Create additional columns for each kmer and fill with zeros
df_kmers =pd.DataFrame(data=np.zeros((df_combined.shape[0],len(kmer_2))), columns=kmer_2)

#Combine df_combiend and df_kmers
df_combined_kmers = pd.concat([df_combined, df_kmers], axis=1)


#Created a nested for loop to update the kmer count for each kmer for each sequence in df_combined_kmers.
for index,row in df_combined_kmers.iterrows():
    for kmer in kmer_2:
        df_combined_kmers.loc[index,[kmer]] = row['Nucleotide Sequence'].count(kmer)
        
df_combined_kmers.to_csv("data_with_2kmer_features.csv", index=False)

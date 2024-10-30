import pandas as pd
from sklearn.model_selection import KFold

#Importing the csv file containing the kmer features for each sequence
df = pd.read_csv("data_with_2kmer_features.csv")

#Dropping the 'Sequence ID' and 'Nucleotide Sequence' columns as they are not necessary for classification
df = df.drop(['Sequence ID', 'Nucleotide Sequence'], axis=1)

#Set the parameters for cv and save to variable kf
kf = KFold(n_splits=5, shuffle=True, random_state=25)

#Saving the labels for each sequence as 'y'
y = df["Label"]

#Saving the features for each sequence as 'x'
x = df.iloc[0:df.shape[0],1:df.shape[1]]

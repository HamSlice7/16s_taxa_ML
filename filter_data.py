#Parsing FASTA file --> https://biopython.org/wiki/SeqIO
#Working with Seq objects --> https://biopython.org/wiki/Seq
import df_from_fasta
import matplotlib.pyplot as plt
import numpy as np


df_enterobacterales = df_from_fasta.df_from_FASTA("enterobacterales.fasta")
df_bacillales = df_from_fasta.df_from_FASTA("bacillales.fasta")


#Filter rows with more more that 5% of the sequence missing

rows_to_remove_bacillales = []
rows_to_remove_enterobacterales = []

for index, row in df_bacillales.iterrows():
    if row["Nucelotide Sequence"].count("N") >= (len(row["Nucelotide Sequence"]) * 0.05):
        rows_to_remove_bacillales.append(index)

for index, row in df_enterobacterales.iterrows():
    if row["Nucelotide Sequence"].count("N") >= (len(row["Nucelotide Sequence"]) * 0.05):
        rows_to_remove_enterobacterales.append(index)

print(len(rows_to_remove_bacillales), len(rows_to_remove_enterobacterales))

##Look at the distribution of the sequence lengths

#Bacillales
bacillales_sequence_lengths = []


for index, row in df_bacillales.iterrows():
    bacillales_sequence_lengths.append(len(row["Nucelotide Sequence"]))

plt.hist(bacillales_sequence_lengths)
plt.xlabel("Sequence Length")
plt.ylabel("Count")
plt.title("Frequency of the sequence of the 16S rRNA geene in Bacillales")
plt.show()

#Enterobacterales
enterobacterales_sequence_lengths = []


for index, row in df_enterobacterales.iterrows():
    enterobacterales_sequence_lengths.append(len(row["Nucelotide Sequence"]))

plt.hist(enterobacterales_sequence_lengths)
plt.xlabel("Sequence Length")
plt.ylabel("Count")
plt.title("Frequency of the sequence of the 16S rRNA geene in Enterobacterales")
plt.show()
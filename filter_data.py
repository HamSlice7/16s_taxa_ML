#Parsing FASTA file --> https://biopython.org/wiki/SeqIO
#Working with Seq objects --> https://biopython.org/wiki/Seq
import df_from_fasta


df_enterobacterales = df_from_fasta.df_from_FASTA("enterobacterales.fasta")
df_bacillales = df_from_fasta.df_from_FASTA("bacillales.fasta")


yes = []

for index, row in df_bacillales.iterrows():
    if row["Nucelotide Sequence"].count("N") >= (len(row["Nucelotide Sequence"]) * 0.05):
        yes.append("yes")

print(len(yes))
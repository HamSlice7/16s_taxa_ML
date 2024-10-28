#Parsing FASTA file --> https://biopython.org/wiki/SeqIO
#Working with Seq objects --> https://biopython.org/wiki/Seq
from Bio import SeqIO
import pandas as pd

def df_from_FASTA(fasta_file:str) -> pd.DataFrame:
    """
    Converts a FASTA file into a panda's data frame. 

    Input:
        - Path to a FASTA file
    Output:
        - Data Frame made up of two columns: Sequence ID and Nucleotide Sequence. Each row
          represents an entry from the inputted FASTA file

    """
    sequence_id = []
    sequence_sequence = []

    for record in SeqIO.parse(fasta_file, "fasta"):
        sequence_id.append(record.id)
        sequence_sequence.append(record.seq)

    sequence_tuples = list(zip(sequence_id,sequence_sequence))

    df = pd.DataFrame(sequence_tuples, columns=["Sequence ID", "Nucelotide Sequence"])

    return df
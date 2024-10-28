#https://biopython.org/docs/dev/Tutorial/chapter_entrez.html#sec-entrez-webenv

from Bio import Entrez

Entrez.email = 'jhambly@uoguelph.ca'

##Searching for 16S rRNA sequences from the NCBI's Nucleotide data base. Filter the sequences to only retrieve lengths from 10000 to 3000 bp as a standard rRNA gene length is around 1500bp. 

#Getting max number of hits for gram negative order of Enterobacterales
Enterobacterales_hits = Entrez.esearch(db = 'nucleotide', term = "Enterobacterales[ORGN] AND 16S rRNA AND biomol_rRNA[PROP] AND 1000:3000[SLEN]", usehistory="y")
record_Enterobacterales_hits = Entrez.read(Enterobacterales_hits)

count = int(record_Enterobacterales_hits["Count"])
webenv = record_Enterobacterales_hits["WebEnv"]
query_key = record_Enterobacterales_hits["QueryKey"]

batch_size = 25

output = open("enterobacterales.fasta", "w")
for start in range(0,count,batch_size):
    end = min(count, start + batch_size)
    print(f"Downloading record {start + 1} to {end}")
    stream = Entrez.efetch(
        db = "nucleotide",
        rettype = "fasta",
        retmode = "text",
        retstart = "start",
        retmax = batch_size,
        webenv = webenv,
        query_key = query_key,
        idtype = "acc"
    )
    data = stream.read()
    stream.close()
    output.write(data)
output.close()
    

#Getting max number of hits for gram positive order of Bacillales
Bacillales_hits = Entrez.esearch(db = 'nucleotide', term = "Bacillales[ORGN] AND 16S rRNA AND biomol_rRNA[PROP] AND 1000:3000[SLEN]", usehistory="y")
record_Bacillales_hits = Entrez.read(Bacillales_hits)

count = int(record_Bacillales_hits["Count"])
webenv = record_Bacillales_hits["WebEnv"]
query_key = record_Bacillales_hits["QueryKey"]


output = open("bacillales.fasta", "w")
for start in range(0,count,batch_size):
    end = min(count, start + batch_size)
    print(f"Downloading record {start + 1} to {end}")
    stream = Entrez.efetch(
        db = "nucleotide",
        rettype = "fasta",
        retmode = "text",
        retstart = "start",
        retmax = batch_size,
        webenv = webenv,
        query_key = query_key,
        idtype = "acc"
    )
    data = stream.read()
    stream.close()
    output.write(data)
output.close()


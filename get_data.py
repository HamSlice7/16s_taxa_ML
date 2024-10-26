from Bio import Entrez

Entrez.email = 'jhambly@uoguelph.ca'

#Searching for 16S rRNA sequences from the NCBI's Nucleotide data base. I filter the sequenes to only get lengths from 10000 to 3000 bp as a standard rRNA gene length is around 1500bp. 
max_Enterobacterales_hits = Entrez.esearch(db = 'nucleotide', term = "Enterobacterales[ORGN] AND 16S rRNA AND biomol_rRNA[PROP] AND 1000:3000[SLEN]")
record = Entrez.read(max_Enterobacterales_hits)


#searching with the max number of hits as the retmax parameter 
Enterobacterales_search = Entrez.esearch(db = 'nucleotide', term = "Enterobacterales[ORGN] AND 16S rRNA AND biomol_rRNA[PROP] AND 1000:3000[SLEN]", retmax = record["Count"], use_history = True)
record_Enterobacterales_search = Entrez.read(Enterobacterales_search)
print(len(record_Enterobacterales_search['IdList']))

max_Bacillales_hits = Entrez.esearch(db = 'nucleotide', term = "Bacillales[ORGN] AND 16S rRNA AND biomol_rRNA[PROP] AND 1000:3000[SLEN]")
record_max_Bacillales_hits = Entrez.read(max_Bacillales_hits)
print(len(record_max_Bacillales_hits['IdList']))
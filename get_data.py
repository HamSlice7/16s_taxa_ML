from Bio import Entrez

Entrez.email = 'jhambly@uoguelph.ca'

##Searching for 16S rRNA sequences from the NCBI's Nucleotide data base. Filter the sequences to only retrieve lengths from 10000 to 3000 bp as a standard rRNA gene length is around 1500bp. 

#Getting max number of hits for gram negative order of Enterobacterales
max_Enterobacterales_hits = Entrez.esearch(db = 'nucleotide', term = "Enterobacterales[ORGN] AND 16S rRNA AND biomol_rRNA[PROP] AND 1000:3000[SLEN]")
record_max_Enterobacterales_hits = Entrez.read(max_Enterobacterales_hits)

#searching with the max number of hits as the retmax parameter (default is 20)
Enterobacterales_search = Entrez.esearch(db = 'nucleotide', term = "Enterobacterales[ORGN] AND 16S rRNA AND biomol_rRNA[PROP] AND 1000:3000[SLEN]", retmax = record_max_Enterobacterales_hits["Count"], use_history = True)
record_Enterobacterales_search = Entrez.read(Enterobacterales_search)

#Getting max number of hits for gram positive order of Bacillales
max_Bacillales_hits = Entrez.esearch(db = 'nucleotide', term = "Bacillales[ORGN] AND 16S rRNA AND biomol_rRNA[PROP] AND 1000:3000[SLEN]")
record_max_Bacillales_hits = Entrez.read(max_Bacillales_hits)

#searching with the max number of hits as the retmax parameter(default is 20)
Bacillales_search = Entrez.esearch(db = 'nucleotide', term = "Bacillales[ORGN] AND 16S rRNA AND biomol_rRNA[PROP] AND 1000:3000[SLEN]", retmax = record_max_Bacillales_hits["Count"], use_history = True)
record_Bacillales_search = Entrez.read(Bacillales_search)


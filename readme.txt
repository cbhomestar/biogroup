ssrfinder.py

CONTENTS
---------------
INTRODUCTION
REQUIREMENTS
HOW TO RUN
RESULTS
FAQ

INTRODUCTION
---------------
ssrfinder.py is a genotyping program designed to compare two samples or two parents to their F2+ children.
Simple SSR's are used to genotype each sample. Compound SSR's are not supported.
The children are genotyped by comparing their SSR's to each parent for matches.
Matches are confirmed by taking the left and right 50 nucleotides and getting an alignment score.
This program uses assembled Next Generation Sequencing (NGS) data.

REQUIREMENTS
---------------
Python 2.7 is required to run the program.
RAM requirements depend on amount of data being inputted, however at least 6-8 GB RAM is recommended.

HOW TO RUN
---------------
The command for executing this program is as follows:
(For two samples) python ssrfinder.py sample1.fa(sta) sample2.fa(sta)
(For parents and children) python ssrfinder.py parent1.fa(sta) parent2.fa(sta) child1.fa(sta) child2.fa(sta) ...

RESULTS
---------------
The following is an explanation of the results generated:

For two samples, a comma separated value (.csv) file called output.csv.
It will have the following heading:
Sample, Label, SSR #, SSR type, SSR, size, Start, End, Left 50, Right 50 
Sample 1 corresponds to the first sample inputted, and Sample 2 to the second.
The Label is the label of the contig for the SSR.
SSR # is an individually generated running SSR #.
SSR type begins with p and ends with the length of the SSR repeat. E.g. AT is a p2 repeat, while ATT is a p3 repeat.
SSR is the SSR repeat in parentheses followed by the number of repeats.
Size corresponds to the full length of the SSR.
Start represents the starting nucleotide of the SSR in the contig.
End represents the ending nucletotide of the SSR in the contig.
The Left 50 corresponds to the (up to) 50 nucleotides to the left of the SSR.
The Right 50 is the same as the Left 50, but for the right of the SSR.

For two parents and children, two .csv files are produced. One called comparisonOutputs.csv; the other HybridTables.csv.
The comparisonOutputs.csv file is very much the same as a output.csv file.
The major difference is that it will also include the children, so for each SSR, each child that has that SSR will be listed under the parents.

The HybridTables.csv works as follows:
The heading is SSR, parent1, parent2, child1, child2, ..., with the sample names (generated from the .fa(sta) file neames) substituted.
The file will list each SSR as the SSR repeat in parentheses, followed by one number (corresponding to parent1's repeat number), a slash, and a second number (corresponding to parent2's repeat number).
Parent1's column will always be A and parent2's will always be B.
The children may be genotyped as follows:
X - similar SSR not found
A - matches only to parent1
B - matches only to parent2
H - matches to both parents, heterozygote
Thus given mapping parents, children can be genotyped.

FAQ
---------------
Q: What file formats are accepted?
A: ssrfinder.py accepts .fa and .fasta file formats. Fastq files are not accepted.

Q: Will your program detect heterozygotes?
A: Yes, our program checks each SSR to see if a heterozygote is possible.

Q: Do I have to assemble my sequences?
A: No, for best results, however, assembling sequence data is recommended.

Q: Can I just compare two organism's SSRS?
A: Yes, the program will produce a table just for two samples when they are the only input.

Q: Can I use this for phylogenetics?
A: As of right now, no. The plan is to add that functionality in the future.

Q: Why do you report the left and right 50 nucleotides?
A: That is to help assist the researcher in finding the sequence, but more importantly for potential primer design.

Q: How long does it take for your program to run?
A: ssrfinder.py can take anywhere from 5 minutes up to a few hours.

#!/usr/bin/env python3

import prob_ba1f as p
import prob_ba1j as j

ecoli_file = "data/ecoli.fasta"
with open(ecoli_file, 'r') as f:
    metadata = f.readline()
    genome = f.read().replace('\n','')


print(metadata)
print(genome[:50])
mins = p.min_skew_points(genome)

print(mins)
subgenome = genome[mins[0] - 500: mins[0] + 500]
result = j.faster_frequent_words(subgenome, 9, distance=1)
print(result)

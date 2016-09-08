#!/usr/bin/env python3

import prob_ba1f as p

ecoli_file = "data/ecoli.fasta"
with open(ecoli_file, 'r') as f:
    metadata = f.readline()
    genome = f.read()


print(metadata)
print(genome[:50])
print(p.min_skew_points(genome))

#!/usr/bin/env python3

import prob_ba1f as ba1f
import prob_ba1j as ba1j

import sys

data_file = sys.argv[1]
with open(data_file, 'r') as f:
    metadata = f.readline()
    genome = f.read().replace('\n','')


print('Working on {} ...'.format(data_file))
print('FASTA metadata: \n  {}'.format(metadata))

## Minimum GC skew points
mins = ba1f.min_skew_points(genome)
print('Minimum GC skew points: \n  {}\n'.format(', '.join(map(str, mins))))

## Frequent Words
subgenome = genome[mins[0]: mins[0] + 500]
kmer_len = 9
distance = 1
with_revc = True

result = ba1j.faster_frequent_words(subgenome, kmer_len, distance=distance, with_revc=with_revc)
print(
"""Frequent words with
  -- window size  : {},
  -- kmer length  : {},
  -- hamming dist : {},
  -- with revc    : {}""".format(len(subgenome), kmer_len, distance, with_revc))
print(result)

## Does the 9-mer exist in common words?
#print("Pattern was found in a set of {}!".format(len(result[0])) if 'TTATCCACA' in result[0] else "Pattern not present")
print()


## Spliting set by revc
def split_by_revc(resultset):
    arbset = set()

    for pattern in sorted(resultset): # Was acting erratic with out this
        revc_pattern = ba1j.reverse_compliment(pattern)
        if revc_pattern not in arbset and pattern not in arbset:
            arbset.add(pattern)

    revcset = resultset ^ arbset
    assert len(arbset) + len(revcset) == len(resultset)

    return (arbset, revcset)


print("Results split into compliment and reverse compliment:")
revc_sets = split_by_revc(result[0])
for i in revc_sets:
    print(sorted(i))
print()


## Find patterns of only hamming distance of 1
def find_close_matches(xset):
    result = set()
    for i in xset:
        for k in xset:
            if ba1j.hamming_distance(i, k) == 1:
                result.add(i)
    return result

found_hamming = [find_close_matches(i) for i in revc_sets]

print("Matches with a hamming distance of 1 for each revc set")
for i in found_hamming:
    print(sorted(i))


#!/usr/bin/env python3

__author__ = 'Kaleb Olson'
__course__ = 'CS418-001'
__problem__ = 'ba1j'
__title__ = 'Frequent words with mismatches and reverse compliment'

import sys
import unittest
from collections import defaultdict


def faster_frequent_words(genome, kmer_len, distance=0, with_revc=True):
    '''A more effecient frequent words algorithm'''
    mutation_dict = defaultdict(int)
    most_frequent = set()

    for i in range(0, len(genome) - kmer_len + 1):
        kmer = genome[i : i + kmer_len]
        mutations = mutate(kmer, distance)

        #if with_revc:
        #    mutations = mutations.union(mutate(reverse_compliment(kmer), distance))

        for mutation in mutations:
            mutation_dict[mutation] += 1
            if with_revc:
                mutation_dict[reverse_compliment(mutation)] += 1

    maxcount = max(mutation_dict.values())
    for kmer, count in mutation_dict.items():
        if count == maxcount:
            most_frequent.add(kmer)

    return most_frequent, maxcount


def mutate(pattern, distance):
    '''Returns the set of patterns that are at
       most d changes away from the original'''

    if distance == 0:
        return set([pattern])
    if len(pattern) == 1:
        return set('ATGC')

    mutations = set()
    suffix = pattern[1:]
    prefix = pattern[:1]
    suffix_mutations = mutate(suffix, distance)

    for mutation in suffix_mutations:
        if hamming_distance(suffix, mutation) < distance:
            for N in 'ATGC':
                mutations.add(N + mutation)
        else:
            mutations.add(prefix + mutation)

    return mutations


def hamming_distance(pattern, pattern_):
    assert len(pattern) == len(pattern_)
    return sum(i != j for i, j in zip(pattern, pattern_))


def reverse_compliment(sequence):
    tr = str.maketrans('ATGC','TACG')
    return sequence.translate(tr)[::-1]


def main(datafile):
    with open(datafile, 'r') as f:
        genome = f.readline().strip()
        k, d = map(int, f.readline().strip().split(' '))

    output = ' '.join(faster_frequent_words(genome, k, d)[0])

    with open('scratch/prob_' + __problem__ + '_output.txt', 'w') as f:
        f.write(output)


class Tests(unittest.TestCase):
    def test_hamming_distance(self):
        self.assertEqual(hamming_distance('abc', 'abc'), 0)
        self.assertEqual(hamming_distance('abc', 'abz'), 1)
        self.assertEqual(hamming_distance('abc', 'ayz'), 2)
        self.assertEqual(hamming_distance('abc', 'xyz'), 3)

    def test_mutate_pattern(self):
        self.assertEqual(mutate('ATGC', 0), set(['ATGC']))
        self.assertEqual(mutate('A', 1), set('ATGC'))
        self.assertEqual(mutate('AA', 1), set(['AA', 'AC', 'AG', 'AT', 'CA', 'GA', 'TA']))
        self.assertEqual(mutate('AA', 2), set(['AA', 'AC', 'GT', 'AG', 'CC', 'CA', 'CG', 'TT', 'GG', 'GC', 'AT', 'GA', 'TG', 'CT', 'TC', 'TA']))
        self.assertTrue(len(mutate('AAA', 3)) == 4 ** 3)

    def test_frequent_with_mismatch(self):
        self.assertEqual(faster_frequent_words('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4, distance=1, with_revc=False)[0], {'GATG', 'ATGC', 'ATGT'} )
        self.assertEqual(faster_frequent_words('AAAAAAAAAA', 2, distance=1, with_revc=False)[0], {'AA', 'AC', 'AG', 'CA', 'AT', 'GA', 'TA'} )
        self.assertEqual(faster_frequent_words('ATA', 3, distance=1, with_revc=False)[0], {'GTA', 'ACA', 'AAA', 'ATC', 'ATA', 'AGA', 'ATT', 'CTA', 'TTA', 'ATG'} )

    def test_frequent_with_revc_and_mismatch(self):
        self.assertEqual(faster_frequent_words('AATTAATTGGTAGGTAGGTA', 4, distance=0)[0], {'AATT'})
        self.assertEqual(faster_frequent_words('AAT', 3, distance=0)[0], {'AAT', 'ATT'})
        self.assertEqual(faster_frequent_words('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4, distance=1, with_revc=True)[0], {'ACAT', 'ATGT'})


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("Missing datafile path! Running tests instead...")
        unittest.main()

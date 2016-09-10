#!/usr/bin/env python3

__author__  = 'Kaleb Olson'
__course__   = 'CS418-001'
__problem__ = 'ba1f'
__title__   = 'Minimum Skew'

import sys
import unittest

def min_skew_points(genome):
    min_skew_indicies = []
    min_skew = 0
    skew = 0
    for i, N in enumerate(genome):
        if N not in 'ATGC':
            print(N)

        if N == 'C':
            skew -= 1
        elif N == 'G':
            skew += 1

        if skew < min_skew:
            min_skew_indicies = [i + 1]
            min_skew = skew
        elif skew == min_skew:
            min_skew_indicies.append(i + 1)
    return min_skew_indicies

def main(datafile):
    with open(datafile, 'r') as f:
        genome = f.readline().strip()

    output =  ' '.join(map(str, min_skew_points(genome)))

    with open('scratch/prob_'+ __problem__ + '_output.txt', 'w') as f:
        f.write(output)

class tests(unittest.TestCase):
    def test_1(self):
        data = 'CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG'
        self.assertEqual(min_skew_points(data), [53, 97])

    def test_2(self):
        data = 'TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'
        self.assertEqual(min_skew_points(data), [11, 24])

    def test_indexing(self):
        self.assertEqual(min_skew_points('ACCG'), [3])

    def test_missing_last(self):
        self.assertEqual(min_skew_points('ACCC'), [4])

    def test_finding_min(self):
        self.assertEqual(min_skew_points('CCGGGT'), [2])

    def test_finding_multiple(self):
        self.assertEqual(min_skew_points('CCGGCCGG'), [2, 6])


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("Missing datafile path! Running tests instead...")
        unittest.main()

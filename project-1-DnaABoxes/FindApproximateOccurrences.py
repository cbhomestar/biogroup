def HammingDistance(string1, string2):
	#check string lengths

	numMismatches = 0

	for i in range(0, len(string1)):
		if string1[i] != string2[i]:
			numMismatches += 1

	return numMismatches

def FindApproximateOccurrences(pattern, genome, allowedDistance):
	locationsOfPattern = []

	for i in range(0, len(genome) - len(pattern)):
		kmer = genome[i : i + len(pattern)]
		hammingDistance = HammingDistance(kmer, pattern)

		if hammingDistance <= allowedDistance:
			locationsOfPattern.append(str(i))

	return locationsOfPattern

if __name__ == "__main__":

	import sys

	pattern = ""
	genome = ""
	allowedDistance = 0

	with open(sys.argv[1]) as file:
		pattern = next(file).strip()
		genome = next(file).strip()
		allowedDistance = int(next(file).strip())

	locationsOfPattern = FindApproximateOccurrences(pattern, genome, allowedDistance)
	print(" ".join(locationsOfPattern))
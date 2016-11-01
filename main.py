def findSSRs(dna, ssr):
	pattern = getPatternFromSSR(ssr)
	matchIndices = [match.span() for match in re.finditer(pattern, dna)]
	return matchIndices

def getPatternFromSSR(ssr):
	repeatNumber = {2: 8, 3: 6, 4: 5, 5: 4}
	pattern = ssr * repeatNumber[len(ssr)]
	return pattern

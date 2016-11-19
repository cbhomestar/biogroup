import re
import sys

class Organism(object):
	def __init__(self, name, file):
		self.name = name
		self.file = file
		self.ssrs = []

	def addSSR(self, ssr):
		self.ssrs.append(ssr)

	def getName(self):
		return self.name
	
	def getListOfSSRs(self):
		return self.ssrs

class SSR:
	pattern = ""
	repeatNum = 0
	totalSize = 0
	contigName = ""
	startLocation = 0
	endLocation = 0
	left50 = ""
	right50 = ""
	label = ""
	number = 0
	def _init_(self, pattern):
		self.pattern=pattern
		totalSize=len(pattern) #i dont know if this is right
	def setPattern(self,pattern):
		self.pattern=pattern
	def getPattern(self):
		return self.pattern
	def setNumber(self,Num):
		self.number=Num
	def getNumber(self):
		return self.number
	def setLabel(self,label):
		self.label=label
	def getLabel(self):
		return self.label
	def setRepeatNum(self,num):
		self.repeatNum=num
	def addToRepeatNum(self,num):
		self.repeatNum+=num
	def getRepeatNum(self):
		return self.repeatNum
	def setTotalSize(self,size):
		self.totalSize=size
	def getTotalSize(self):
		return self.totalSize
	def setContigName(self,name):
		self.contigName=name
	def getContigName(self):
		return self.contigName
	def setStartLocation(self,start):
		self.startLocation=start
	def getStartLocation(self):
		return self.startLocation
	def setEndLocation(self,end):
		self.endLocation=end
	def getEndLocation(self):
		return self.endLocation
	def setLeft50(self,left):
		self.left50=left
	def getLeft50(self):
		return self.left50
	def setRight50(self,right):
		self.right50=right
	def getRight50(self):
		return self.right50
	
def calculatePossibleSSRs(myNum):
	myKmers=list()
	nucleotides=('A','T','G','C')
	for i in range(2,int(myNum)+1):
		imers=list()
		for j in range(i): #for each element
			if len(imers)==0:
				for n in nucleotides:
					imers.append(n)
			else:
				newImers=list();
				for myString in imers:
					for n in nucleotides:
						newImers.append(myString+n)
				imers=newImers
		for result in imers:
			if len(result)%2==0:
				if result[0:len(result)/2]!=result[len(result)/2:len(result)]:
					myKmers.append(result)
			else:
				ok=False
				start=result[0]
				for i in range(1,len(result)):
					if result[i]!=start:
						ok=True
				if ok:
					myKmers.append(result)
	return myKmers

def compareSeqs(s1, s2):
	if (len(s1) <= 7) or (len(s2) <= 7):
		return False
	s1.upper()
	s2.upper()
	matrix = [[0 for x in range(len(s2) + 1)] for y in range(len(s1) + 1)]
	gap = -1
	mismatch = 0
	match = 1
	maxscore = 0
	score1 = 0
	score2 = 0
	score3 = 0
	for i in range(1, len(s1) + 1):
		matrix[i][0] = gap + matrix[i - 1][0]
	for j in range(1, len(s2) + 1):
		matrix[0][j] = gap + matrix[0][j - 1]
	for i in range(1, len(s1) + 1):
		for j in range(1, len(s2) + 1):
			if (s1[i - 1] == s2[j - 1]):
				score1 = matrix[i - 1][j - 1] + match
			else:
				score1 = matrix[i - 1][j - 1] + mismatch
			score2 = matrix[i][j - 1] + gap
			score3 = matrix[i - 1][j] + gap
			matrix[i][j] = max(score1, score2, score3)
			if matrix[i][j] > maxscore:
				maxscore = matrix[i][j]
	if maxscore >= (.85 * min(len(s1), len(s2))):
		return True
	return False

def findSSRs(dna, ssr):
	pattern = getPatternFromSSR(ssr)
	matchIndices = [match.span() for match in re.finditer(pattern, dna)]
	return matchIndices

def getPatternFromSSR(ssr):
	repeatNumber = {2: 8, 3: 6, 4: 5, 5: 4}
	pattern = ssr * repeatNumber[len(ssr)]
	return pattern

def reverseComplement(seq):
	output = ""
	seq = seq[::-1]
	for letter in seq:
		if letter == 'A':
			output += "T"
		if letter == 'C':
			output += "G"
		if letter == 'G':
			output += "C"
		if letter == 'T':
			output += "A"
		if letter == 'N':
			output += "N"
	return output
			
organismList = []
for i in (range(1, len(sys.argv))):
           with open(sys.argv[i]) as file:
		fileName = sys.argv[i]
		name = fileName.split('.')[0]
		organism = Organism(name, file)
                sequences = {}
                label = ""
                sequence = ""
                sequenceNumber = 0
                for line in file:
                	line = line.strip()
                	if (line[0] == ">"):
                		if (sequenceNumber > 0):
                			sequences[label] = sequence
                			label = line[1:]
                			sequence = ""
                 			sequenceNumber += 1
                		else:
                 			label = line[1:]
                			sequenceNumber += 1
			else:
                		sequence += line
		sequences[label]=sequence
		kmers = []
		ssrNumber = 1
		for j in range(2, 6):
			kmers = calculatePossibleSSRs(j)
			for kmer in kmers:
				for label in sequences:
					sequence = sequences[label]
					foundSSRS = findSSRs(sequence, kmer)
					for index in foundSSRS:
						newSSR = SSR()
						newSSR.setLabel(label)
						newSSR.setPattern(kmer)
						newSSR.setNumber(ssrNumber)
						ssrNumber += 1
						newSSR.setContigName(label)
						newSSR.setStartLocation(index[0])
						k = 0
						while sequence[(index[0] + k * len(kmer)): (index[0] + k * len(kmer) + len(kmer))] == kmer:
							k += 1
						newSSR.setRepeatNum(k)
						newSSR.setEndLocation(index[0] + k * len(kmer) - 1)
						newSSR.setTotalSize(k * len(kmer))
						if (index[0] < 50):
							newSSR.setLeft50(sequence[0:(index[0])])
						else:
							newSSR.setLeft50(sequence[(index[0] - 50): (index[0])])
						if (newSSR.getEndLocation() + 50) > len(sequence):
							newSSR.setRight50(sequence[newSSR.getEndLocation():])
						else:
							newSSR.setRight50(sequence[newSSR.getEndLocation():newSSR.getEndLocation() + 50]) 
						organism.addSSR(newSSR)
		organismList.append(organism)
if (len(organismList) == 2):
	outFile = open("output.csv", 'w')
	outFile.write("Sample,Label,SSR #,SSR type,SSR,size,Start,End,Left 50,Right 50\n")
	ssrList1 = organismList[0].getListOfSSRs()
	ssrList2 = organismList[1].getListOfSSRs()
	for i in range(len(ssrList1)):
		ssr1 = ssrList1[i]
		for j in range(len(ssrList2)):
			ssr2 = ssrList2[j]
			if (ssr1.getPattern() == ssr2.getPattern() and ssr1.getRepeatNum() != ssr2.getRepeatNum() and compareSeqs(ssr1.getLeft50(), ssr2.getLeft50()) and compareSeqs(ssr1.getRight50(), ssr2.getRight50())):
				outFile.write("1," + ssr1.getLabel() + "," + str(ssr1.getNumber()) + ",p" + str(len(ssr1.getPattern())) + ",(" + ssr1.getPattern() + ")" + str(ssr1.getTotalSize() / len(ssr1.getPattern())) + "," + str(ssr1.getTotalSize()) + "," + str(ssr1.getStartLocation()) + "," + str(ssr1.getEndLocation()) + "," + ssr1.getLeft50() + "," + ssr1.getRight50() + '\n')
				outFile.write("2," + ssr2.getLabel() + "," + str(ssr2.getNumber()) + ",p" + str(len(ssr2.getPattern())) + ",(" + ssr2.getPattern() + ")" + str(ssr2.getTotalSize() / len(ssr2.getPattern())) + "," + str(ssr2.getTotalSize()) + "," + str(ssr2.getStartLocation()) + "," + str(ssr2.getEndLocation()) + "," + ssr2.getLeft50() + "," + ssr2.getRight50() + '\n')
			if (ssr1.getPattern() == reverseComplement(ssr2.getPattern()) and ssr1.getRepeatNum() != ssr2.getRepeatNum() and compareSeqs(ssr1.getLeft50(), reverseComplement(ssr2.getRight50())) and compareSeqs(ssr1.getRight50(), reverseComplement(ssr2.getLeft50()))):
				outFile.write("1," + ssr1.getLabel() + "," + str(ssr1.getNumber()) + ",p" + str(len(ssr1.getPattern())) + ",(" + ssr1.getPattern() + ")" + str(ssr1.getTotalSize() / len(ssr1.getPattern())) + "," + str(ssr1.getTotalSize()) + "," + str(ssr1.getStartLocation()) + "," + str(ssr1.getEndLocation()) + "," + ssr1.getLeft50() + "," + ssr1.getRight50() + '\n')
				outFile.write("2," + ssr2.getLabel() + "," + str(ssr2.getNumber()) + ",p" + str(len(ssr2.getPattern())) + ",(" + ssr2.getPattern() + ")" + str(ssr2.getTotalSize() / len(ssr2.getPattern())) + "," + str(ssr2.getTotalSize()) + "," + str(ssr2.getStartLocation()) + "," + str(ssr2.getEndLocation()) + "," + ssr2.getLeft50() + "," + ssr2.getRight50() + '\n')
	outFile.close()
if (len(organismList) > 2):
	outFile = open("comparisonOutput.csv", 'w')
	outFile.write("Sample,Label,SSR #,SSR type,SSR,size,Start,End,Left 50,Right 50\n")
	ssrList1 = organismList[0].getListOfSSRs()
	ssrList2 = organismList[1].getListOfSSRs()
	for i in range(len(ssrList1)):
		ssr1 = ssrList1[i]
		for j in range(len(ssrList2)):
			ssr2 = ssrList2[j]
			if (ssr1.getPattern() == ssr2.getPattern() and ssr1.getRepeatNum() != ssr2.getRepeatNum() and compareSeqs(ssr1.getLeft50(), ssr2.getLeft50()) and compareSeqs(ssr1.getRight50(), ssr2.getRight50())):
				outFile.write("1," + ssr1.getLabel() + "," + str(ssr1.getNumber()) + ",p" + str(len(ssr1.getPattern())) + ",(" + ssr1.getPattern() + ")" + str(ssr1.getTotalSize() / len(ssr1.getPattern())) + "," + str(ssr1.getTotalSize()) + "," + str(ssr1.getStartLocation()) + "," + str(ssr1.getEndLocation()) + "," + ssr1.getLeft50() + "," + ssr1.getRight50() + '\n')
				outFile.write("2," + ssr2.getLabel() + "," + str(ssr2.getNumber()) + ",p" + str(len(ssr2.getPattern())) + ",(" + ssr2.getPattern() + ")" + str(ssr2.getTotalSize() / len(ssr2.getPattern())) + "," + str(ssr2.getTotalSize()) + "," + str(ssr2.getStartLocation()) + "," + str(ssr2.getEndLocation()) + "," + ssr2.getLeft50() + "," + ssr2.getRight50() + '\n')
			for k in range(2, len(organismList)):
				childSSRs = organismList[k].getListOfSSRs()
				for l in range(len(childSSRs)):
					ssrC = childSSRs[l]
					if (ssr1.getPattern() == ssrC.getPattern() and compareSeqs(ssr1.getLeft50(), ssrC.getLeft50()) and compareSeqs(ssr1.getRight50(), ssrC.getRight50())):
						outFile.write("1," + ssrC.getLabel() + "," + str(ssrC.getNumber()) + ",p" + str(len(ssrC.getPattern())) + ",(" + ssrC.getPattern() + ")" + str(ssrC.getTotalSize() / len(ssrC.getPattern())) + "," + str(ssrC.getTotalSize()) + "," + str(ssrC.getStartLocation()) + "," + str(ssrC.getEndLocation()) + "," + ssrC.getLeft50() + "," + ssrC.getRight50() + '\n')

			if (ssr1.getPattern() == reverseComplement(ssr2.getPattern()) and ssr1.getRepeatNum() != ssr2.getRepeatNum() and compareSeqs(ssr1.getLeft50(), reverseComplement(ssr2.getRight50())) and compareSeqs(ssr1.getRight50(), reverseComplement(ssr2.getLeft50()))):
				outFile.write("1," + ssr1.getLabel() + "," + str(ssr1.getNumber()) + ",p" + str(len(ssr1.getPattern())) + ",(" + ssr1.getPattern() + ")" + str(ssr1.getTotalSize() / len(ssr1.getPattern())) + "," + str(ssr1.getTotalSize()) + "," + str(ssr1.getStartLocation()) + "," + str(ssr1.getEndLocation()) + "," + ssr1.getLeft50() + "," + ssr1.getRight50() + '\n')
				outFile.write("2," + ssr2.getLabel() + "," + str(ssr2.getNumber()) + ",p" + str(len(ssr2.getPattern())) + ",(" + ssr2.getPattern() + ")" + str(ssr2.getTotalSize() / len(ssr2.getPattern())) + "," + str(ssr2.getTotalSize()) + "," + str(ssr2.getStartLocation()) + "," + str(ssr2.getEndLocation()) + "," + ssr2.getLeft50() + "," + ssr2.getRight50() + '\n')
	outFile.close()
	outFile2 = open("HybridTables.csv","w")
	outFile2.write("SSR")
	for i in range(len(organismList)):
		outFile2.write("," + organismList[i].getName())
	outFile2.write('\n')
	ssrList1 = organismList[0].getListOfSSRs()
	ssrList2 = organismList[1].getListOfSSRs()
	for ssr1 in ssrList1:
		for ssr2 in ssrList2:
			if (ssr1.getPattern() == ssr2.getPattern() or ssr1.getPattern() == reverseComplement(ssr2.getPattern())) and ssr1.getRepeatNum() != ssr2.getRepeatNum() and (compareSeqs(ssr1.getLeft50(), ssr2.getLeft50()) and compareSeqs(ssr1.getRight50(), ssr2.getRight50()) or compareSeqs(ssr1.getLeft50(), reverseComplement(ssr2.getRight50)) and compareSeqs(ssr1.getRight50(), reverseComplement(ssr2.getLeft50()))):
				outFile2.write("(" + ssr1.getPattern() + ")")
				outFile2.write(str(ssr1.getTotalSize() / len(ssr1.getPattern())) + "/" + str(ssr2.getTotalSize() / len(ssr2.getPattern())))
				outFile2.write(",A,B")
				for i in range(2, len(organismList)):
					childSSRs = organismList[i]
					p1 = False
					p2 = False
					for ssrC in childSSRs:
						if (ssr1.getPattern() == ssrC.getPattern() or ssr1.getPattern() == reverseComplement(ssrC.getPattern())) and ssr1.getTotalSize() == ssrC.getTotalSize() and (compareSeqs(ssr1.getLeft50(), ssrC.getLeft50()) and compareSeqs(ssr1.getRight50(), ssrC.getRight50()) or compareSeqs(ssr1.getLeft50(), reverseComplement(ssrC.getRight50())) and compareSeqs(ssr1.getRight50(), reverseComplement(ssrC.getLeft50()))):
							p1 = True
						if (ssr2.getPattern() == ssrC.getPattern() and ssr2.getTotalSize() == ssrC.getTotalSize() and compareSeqs(ssr2.getLeft50(), ssrC.getLeft50()) and compareSeqs(ssr2.getRight50(), ssrC.getRight50())):
							p2 = True
						if p1 and p2:
							outFile2.write(",H")
						elif p1:
							outFile2.write(",A")
						elif p2:
							outFile2.write(",B")
						else:
							outFile2.write(",X")
				outFile2.write("\n")
	outFile.close()


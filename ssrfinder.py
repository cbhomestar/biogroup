import sys

class SSR:
	pattern
	repeatNum=0
	totalSize
	contigName
	startLocation
	endLocation
	left50
	right50
	def _init_(self, pattern):
		self.pattern=pattern
		totalSize=len(pattern) #i dont know if this is right
	def setPattern(self,pattern):
		self.pattern=pattern
	def getPattern(self):
		return self.pattern
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
	if not myNum.isdigit():
		print "ERROR: You need to insert a digit for max kmer size"
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
					print result
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
	if maxscore >= (.85 * min(len(s1), len(s2)):
		return True
	return False

for i in (range(1, len(sys.argv))):
           with open(sys.argv[i]) as file:
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

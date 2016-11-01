#Put your code here
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

#Put your code here
import sys

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

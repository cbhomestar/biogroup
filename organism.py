class Organism(object):
	def __init__(name, file):
		self.name = name
		self.file = file
		self.ssrs = []

	def addSSR(ssr):
		self.ssrs.append(ssr)

	def getListOfSSRs():
		return self.ssrs

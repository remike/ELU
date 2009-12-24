import sys, random

class dTile:
	
	def __init__(self,type='#'):
		self.type = type

class dMap:
	
	px = 1
	py = 1
	
	def __init__(self,w,h,seed):
		self.width = w
		self.height = h
		self.genSeed = seed
		self.map = [[dTile() for i in range(h) ] for j in range(w)  ]
		self.accessible = self.genTerrain()
		self.pMove(2,2)
	
	def genTerrain(self):
		random.seed(self.genSeed)
		nr = random.randint(3,5)
		for i in range(nr):
			x = random.randint(0,self.width)
			y = random.randint(0,self.height)
			w = random.randint(0,self.width/2)
			h = random.randint(0,self.height/2)
			s = max(0,x-w/2)
			t = max(0,y-h/2)
			for a in range(w):
				for b in range(h):
					self.map[min(a+s,self.width-1)][min(b+t,self.height-1)].type="."
		if self.map[2][2].type != ".":
			return "-1"
	def debugPrint(self):
		lines = [ ]
		for i in range(self.width):
			x = ' '
			for j in range(self.height):
				x += self.map[i][j].type
			lines.append(x)
		#lines.append(self.genSeed)
		#lines.append('-' * self.width + '--')
		return lines

	
	def pMove(self,y,x):
		self.map[self.px][self.py].type = '#'
		self.px += x
		self.py += y
		self.map[self.px][self.py].type = '@'

class dWorld:
	
	
	def __init__(self):
		self.gMap = { }
		self.activeMap = 0
		self.scanArea = 11
		self.scanCenter = [0,0]
		self.scan()
	
	def scan(self):
		#print 'Scanning.'
		posX = self.scanCenter[0]-self.scanArea/2
		posY = self.scanCenter[1]-self.scanArea/2
		lines = [ ]
		for i in range(self.scanArea):
			x = " "
			for j in range(self.scanArea):
				if posX == self.scanCenter[0] and posY == self.scanCenter[1]:
					x += 'X'
				else:
					if self.chooseWorld(posX,posY,0)!='-1':
						x += "@"
					else:
						x += "."
				posX+=1
			posX = self.scanCenter[0]-self.scanArea/2
			posY += 1
			lines.append(x)
		return lines
		#	print x
		#print 'Done.'
				
	def chooseWorld(self,x,y,active=0):
		if x>0:
			if y>0:
				s = int(str(1+x)+"0"+str(y))
			else:
				s = int(str(1+x)+"07")
		else:
			if y>0:
				s = int("90"+str(y))-(1+x)
			else:
				s = 907-(1+x)-y
		t = str(x)+":"+str(y)
		self.gMap[t] = dMap(25,30,s)
		if active == 1:
			self.gMap[t].debugPrint()
			self.activeMap = self.gMap[t]
		return self.gMap[t].accessible
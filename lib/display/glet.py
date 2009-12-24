import sys, random
import pyglet

class screen:
	
	def __init__(self):
		self.scr = pyglet.window.Window(800,600)
		self.windows = [ ]
		self.mainW = window(self.scr,0,100,500,400)
		self.topW = window(self.scr,0,500,500,100)
		self.bottomW = window(self.scr,0,0,500,100)
		self.mapW = window(self.scr,500,400,300,200)
		self.rightW = window(self.scr,500,0,300,400)
		self.mainW.debug("Main Test.")
		self.topW.debug("Top Test.")
		self.bottomW.debug("Bottom Test.")
		self.mapW.debug("Map Test.")
		self.rightW.debug("Right-hand Test.")
		self.windows.append(self.mainW)
		self.windows.append(self.topW)
		self.windows.append(self.bottomW)
		self.windows.append(self.mapW)
		self.windows.append(self.rightW)
	
	def refresh(self):
		self.scr.clear()
		for w in self.windows:
			w.refresh()

	def mapPrint(self,lines,x):
		self.mainW.textPrint(lines,x)	
		
	def secPrint(self,lines,x):
		self.mapW.textPrint(lines,x)
	
	def wait(self):
		pass
	
	def end(self):
		pass
	
class window:
	
	def __init__(self,scr,x,y,width,height):
		self.scr = scr
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.objects = [ ]
		self.debugLabel = 0
		self.labels = [ ]
		
		
	def debug(self,msg):
		self.debugLabel = pyglet.text.Label(msg,
							font_name='Times New Roman',
							font_size=24,
							x=self.x+(self.width)//2, y=self.y+(self.height)//2,
							anchor_x='center', anchor_y='center')
	
	def drawRelative(self,obj,x,y,w,h):
		self.objects.append( [obj,x+self.x,y+self.y,w,h] )
	
	def textPrint(self,lines,offset):
		
		sx = offset
		sy = self.height-30
		
		hash = pyglet.resource.image('images/hash.png')
		dot = pyglet.resource.image('images/dot.png')
		at = pyglet.resource.image('images/at.png')
		exx = pyglet.resource.image('images/x.png')
		
		
		for i in lines:
			for j in i:
				if j == "#":
					self.drawRelative(hash,sx,sy,15,15)
				elif j == ".":
					self.drawRelative(dot,sx,sy,15,15)
				elif j == "@":
					self.drawRelative(at,sx,sy,15,15)
				elif j == "X":
					self.drawRelative(exx,sx,sy,15,15)
				sx += 15
			sy -= 15
			sx = offset
	
	def refresh(self):
		if self.debugLabel != 0:
			self.debugLabel.draw()
			pyglet.graphics.draw(6, pyglet.gl.GL_LINE_LOOP,
				('v2i',(self.x,self.y,self.x+self.width,self.y,
					self.x+self.width,self.y+self.height,
					self.x+self.width,self.y+self.height,
					self.x,self.y+self.height,self.x,self.y)),
				('c3B', (0,0,255, 0,0,255, 0,0,255,
					0,0,255, 0,0,255, 0,0,255)))
		if len(self.objects) != 0:
			for l in self.objects:
				l[0].blit(l[1],l[2])
		if len(self.labels) != 0:
			for label in self.labels:
				label.draw()
	
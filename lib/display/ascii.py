import sys, random
import curses

class screen:
	
	def __init__(self):
		self.scr = curses.initscr()
		curses.noecho()
		curses.cbreak()
		self.scr.keypad(1)
		curses.init_pair(2,curses.COLOR_GREEN,
			curses.COLOR_BLACK)
		curses.init_pair(3,curses.COLOR_WHITE,
			curses.COLOR_BLACK)
		self.mainW = window(self.scr,20,50,6,0)
		self.topW = window(self.scr,6,50,0,0)
		self.bottomW = window(self.scr,4,50,26,0)
		self.mainW.debug("test")
		self.topW.debug("toptest")
		self.bottomW.debug("bottomtest")
		self.redraw()
	
	def redraw(self):
		self.mainW.refresh()
		self.topW.refresh()
		self.bottomW.refresh()
	
	def wait(self):
		x = self.scr.getch()
		return x
	
	def end(self):
		curses.nocbreak()
		self.scr.keypad(0)
		curses.echo()
		curses.endwin()

		
class window:
	
	def __init__(self,scr,height,width,x,y):
		self.win = curses.newwin(height,width,y,x)
	
	def debug(self,msg):
		self.win.addstr(2,2,msg,curses.color_pair(2))
	
	def refresh(self):
		self.win.refresh()
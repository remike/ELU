from lib.elu import base
from lib.display import glet
import pyglet

	
x = glet.screen()
world = base.dWorld()
world.chooseWorld(5,0,1)


@x.scr.event
def on_draw():
	x.refresh()
	x.mapPrint(world.activeMap.debugPrint(),15)
	x.secPrint(world.scan(),50)

@x.scr.event
def on_key_press(symbol,modifiers):
	t = world.activeMap
	if symbol == pyglet.window.key.A:
		t.pMove(-1,0)
	elif symbol == pyglet.window.key.D:
		t.pMove(1,0)
	elif symbol == pyglet.window.key.W:
		t.pMove(0,-1)
	elif symbol == pyglet.window.key.S:
		t.pMove(0,1)
	
pyglet.app.run()
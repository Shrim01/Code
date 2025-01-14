import collections.abc
import keyboard
import time

collections.Iterable = collections.abc.Iterable
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
x=10
y=10
z=10
flag = True
while True:
    if keyboard.is_pressed("*") and flag:
        flag = False
        pos = mc.player.getPos()
        mc.setBlocks(pos,pos.x+x, pos.y+y, pos.z+z,46)
    else:
        time.sleep(5)
        flag = True
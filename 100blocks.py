import collections.abc
collections.Iterable = collections.abc.Iterable
from mcpi.minecraft import Minecraft
import random
import time

mc = Minecraft.create()

for i in range(128,0,-1):
    if mc.getBlock(0,i,0)!=0:
        height = i
        print(height)
        break

mc.player.setTilePos(0,height+5,0)

mc.setBlocks(0,height+1,0,101,128,0,0)

for i in range(101):
    mc.setBlock(i,height,0,random.randint(0,107))
    time.sleep(1)
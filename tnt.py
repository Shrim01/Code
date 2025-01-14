import collections.abc
collections.Iterable = collections.abc.Iterable

from mcpi.minecraft import Minecraft
import keyboard

mc = Minecraft.create()

x=50
y=0
z=50
while True:
    if  keyboard.is_pressed("*"):
        positionPaste=mc.player.getPos()
        mc.setBlocks(positionPaste,positionPaste.x+x,positionPaste.y+y, positionPaste.z+z,46)
        positionPaste.y+=1
        mc.setBlocks(positionPaste,positionPaste.x+x,positionPaste.y+y, positionPaste.z+z,76)
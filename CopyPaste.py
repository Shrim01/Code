import collections.abc
import time

import keyboard

collections.Iterable = collections.abc.Iterable
from mcpi.minecraft import Minecraft
file = open("postoika.txt","w")
mc = Minecraft.create()

count = 5
while not keyboard.is_pressed("*"):
    i = 0
mc.postToChat("Start Copy")
position = mc.player.getPos()
copy = []
supCopy = []
supSupCopy = []
for i in range(count):
    for j in range(count):
        for k in range(count):
            supSupCopy.append(mc.getBlock(position.x+k,position.y+i, position.z+j))
        supCopy.append(supSupCopy)
        supSupCopy = []
    copy.append(supCopy)
    supCopy = []
    print(i)
mc.postToChat("Finish copy")
mc.postToChat("You can paste if press \"*\"")
file.write(str(copy))
print("good")
while not keyboard.is_pressed("*"):
    i = 0
mc.postToChat("Start Paste")
positionPaste = mc.player.getPos()
for i in range(count):
    for j in range(count):
        for k in range(count):
            mc.setBlock(positionPaste.x+k,positionPaste.y+i, positionPaste.z+j,copy[i][j][k])
            time.sleep(0.05)
mc.postToChat("Finish")
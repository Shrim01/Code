import collections.abc
collections.Iterable = collections.abc.Iterable
from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3
import time
import keyboard


def Paste(pos):
    mc.setBlock(pos.x-1,pos.y,pos.z-1,46)
    mc.setBlock(pos.x+1,pos.y,pos.z-1,46)
    mc.setBlock(pos.x-1,pos.y,pos.z+1,46)
    mc.setBlock(pos.x+1,pos.y,pos.z+1,46)

def PasteCross(pos):
    Paste(pos)
    mc.setBlock(pos.x,pos.y,pos.z,46)

def PasteZero(pos):
    Paste(pos)
    mc.setBlock(pos.x+1,pos.y,pos.z,46)
    mc.setBlock(pos.x-1,pos.y,pos.z,46)
    mc.setBlock(pos.x,pos.y,pos.z+1,46)
    mc.setBlock(pos.x,pos.y,pos.z-1,46)

def Check(num,pas):
    if keyboard.is_pressed(str(num+1)) and flag[num]:
        flag[num]=False
        if pas:
            PasteCross(array[num])
        else:
            PasteZero(array[num])
        return not pas
    return pas

mc = Minecraft.create()

start = Vec3(300000, 90, 300000)
mc.setBlock(start.x + 8, 105, start.z + 8, 20)
mc.player.setPos(start.x + 8.5, 105 + 1, start.z + 8.5)

mc.setBlocks(start, start.x + 16, start.y, start.z + 16, 57)

mc.setBlocks(start.x + 5, start.y + 1, start.z, start.x + 5, start.y + 1, start.z + 16, 57)
mc.setBlocks(start.x + 11, start.y + 1, start.z, start.x + 11, start.y + 1, start.z + 16, 57)
mc.setBlocks(start.x, start.y + 1, start.z + 5, start.x + 16, start.y + 1, start.z + 5, 57)
mc.setBlocks(start.x, start.y + 1, start.z + 11, start.x + 16, start.y + 1, start.z + 11, 57)

array = [start + Vec3(2, 1, 2),
         start + Vec3(2, 1, 8),
         start + Vec3(2, 1, 14),
         start + Vec3(8, 1, 2),
         start + Vec3(8, 1, 8),
         start + Vec3(8, 1, 14),
         start + Vec3(14, 1, 2),
         start + Vec3(14, 1, 8),
         start + Vec3(14, 1, 14)]

flag = [True for i in range(9)]
paste = True
while True:
    for i in range(9):
        paste = Check(i,paste)
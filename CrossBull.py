import collections.abc
collections.Iterable = collections.abc.Iterable
from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3
import keyboard

mc = Minecraft.create()

start = Vec3(3000000, 90, 3000000)
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
    if keyboard.is_pressed("1") and flag[0]:
        pos = array[0]
        if paste:
            mc.setBlock(pos.x - 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x - 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x, pos.y, pos.z, 46)
        else:
            mc.setBlock(pos.x - 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x - 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z, 46)
            mc.setBlock(pos.x - 1, pos.y, pos.z, 46)
            mc.setBlock(pos.x, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x, pos.y, pos.z - 1, 46)
        flag[0] = False
        paste = not paste
    if keyboard.is_pressed("2") and flag[1]:
        pos = array[1]
        if paste:
            mc.setBlock(pos.x - 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x - 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x, pos.y, pos.z, 46)
        else:
            mc.setBlock(pos.x - 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x - 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z, 46)
            mc.setBlock(pos.x - 1, pos.y, pos.z, 46)
            mc.setBlock(pos.x, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x, pos.y, pos.z - 1, 46)
        flag[1] = False
        paste = not paste
    if keyboard.is_pressed("3") and flag[2]:
        pos = array[2]
        if paste:
            mc.setBlock(pos.x - 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x - 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x, pos.y, pos.z, 46)
        else:
            mc.setBlock(pos.x - 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x - 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z, 46)
            mc.setBlock(pos.x - 1, pos.y, pos.z, 46)
            mc.setBlock(pos.x, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x, pos.y, pos.z - 1, 46)
        flag[2] = False
        paste = not paste
    if keyboard.is_pressed("4") and flag[3]:
        pos = array[3]
        if paste:
            mc.setBlock(pos.x - 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x - 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x, pos.y, pos.z, 46)
        else:
            mc.setBlock(pos.x - 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x - 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z, 46)
            mc.setBlock(pos.x - 1, pos.y, pos.z, 46)
            mc.setBlock(pos.x, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x, pos.y, pos.z - 1, 46)
        flag[3] = False
        paste = not paste
    if keyboard.is_pressed("5") and flag[4]:
        pos = array[4]
        if paste:
            mc.setBlock(pos.x - 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x - 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x, pos.y, pos.z, 46)
        else:
            mc.setBlock(pos.x - 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x - 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z, 46)
            mc.setBlock(pos.x - 1, pos.y, pos.z, 46)
            mc.setBlock(pos.x, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x, pos.y, pos.z - 1, 46)
        flag[4] = False
        paste = not paste
    if keyboard.is_pressed("6") and flag[5]:
        pos = array[5]
        if paste:
            mc.setBlock(pos.x - 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x - 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x, pos.y, pos.z, 46)
        else:
            mc.setBlock(pos.x - 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x - 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z, 46)
            mc.setBlock(pos.x - 1, pos.y, pos.z, 46)
            mc.setBlock(pos.x, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x, pos.y, pos.z - 1, 46)
        flag[5] = False
        paste = not paste
    if keyboard.is_pressed("7") and flag[6]:
        pos = array[6]
        if paste:
            mc.setBlock(pos.x - 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x - 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x, pos.y, pos.z, 46)
        else:
            mc.setBlock(pos.x - 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x - 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z, 46)
            mc.setBlock(pos.x - 1, pos.y, pos.z, 46)
            mc.setBlock(pos.x, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x, pos.y, pos.z - 1, 46)
        flag[6] = False
        paste = not paste
    if keyboard.is_pressed("8") and flag[7]:
        pos = array[7]
        if paste:
            mc.setBlock(pos.x - 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x - 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x, pos.y, pos.z, 46)
        else:
            mc.setBlock(pos.x - 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x - 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z, 46)
            mc.setBlock(pos.x - 1, pos.y, pos.z, 46)
            mc.setBlock(pos.x, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x, pos.y, pos.z - 1, 46)
        flag[7] = False
        paste = not paste
    if keyboard.is_pressed("9") and flag[8]:
        pos = array[8]
        if paste:
            mc.setBlock(pos.x - 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x - 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x, pos.y, pos.z, 46)
        else:
            mc.setBlock(pos.x - 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z - 1, 46)
            mc.setBlock(pos.x - 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x + 1, pos.y, pos.z, 46)
            mc.setBlock(pos.x - 1, pos.y, pos.z, 46)
            mc.setBlock(pos.x, pos.y, pos.z + 1, 46)
            mc.setBlock(pos.x, pos.y, pos.z - 1, 46)
        flag[8] = False
        paste = not paste
import collections.abc

collections.Iterable = collections.abc.Iterable
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

position = mc.player.getPos()
for i in range(101):
    mc.spawnEntity(position,45)
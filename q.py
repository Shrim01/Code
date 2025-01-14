import collections.abc
collections.Iterable = collections.abc.Iterable
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

mc.setBlocks(-29000000,1,-29000000,29000000,127,29000000,0)
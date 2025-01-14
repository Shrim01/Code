import collections.abc

collections.Iterable = collections.abc.Iterable
import keyboard

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

count = len(mc.player.pollChatPosts())
while not keyboard.is_pressed("*"):
    print(1)
print(mc.player.pollChatPosts())
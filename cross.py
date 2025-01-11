import collections.abc
collections.Iterable = collections.abc.Iterable
from mcpi.minecraft import Minecraft
import keyboard
mc=Minecraft.create()

key1 = "5"
x = 0
y = 0
z = 0

while True:
    if keyboard.is_pressd("5"):
        mc.SetBlock(x+1,y,z+1,46)
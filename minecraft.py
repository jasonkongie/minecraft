from mcpi.minecraft import Minecraft
import collections
collections.Iterable = collections.abc.Iterable\
                       
mc = Minecraft.create()
x,y,z = mc.player.getPos()
print(x, y, z)

mc.player.setPos(x, y+20, z)
x,y,z = mc.player.getPos()
print(x, y, z)
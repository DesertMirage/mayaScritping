import maya.cmds as cmds


size=10


cmds.polySphere(n="Sun", r=size*10.0)

cmds.polySphere(n="Earth", r=size*1.0)

cmds.polySphere(n="Moon", r=size*0.3)


cmds.circle(n="Sun_Ctrl", r=size*11.0, nr=(0,1,0))

cmds.circle(n="Earth_Ctrl", r=size*1.1, nr=(0,1,0))

cmds.circle(n="Moon_Ctrl", r=size*0.33, nr=(0,1,0))


cmds.color("Sun", rgb=(1,1,0))

cmds.color("Earth", rgb=(0,0,1))

cmds.color("Moon", rgb=(.5,.5,.5))


cmds.parent("Sun", "Sun_Ctrl")

cmds.parent("Earth", "Earth_Ctrl")

cmds.parent("Moon", "Moon_Ctrl")

cmds.parent("Earth_Ctrl", "Sun_Ctrl")

cmds.parent("Moon_Ctrl", "Earth_Ctrl")


cmds.setAttr("Earth_Ctrl.tz", size*20.0)

cmds.setAttr("Moon_Ctrl.tz", size*3.0)
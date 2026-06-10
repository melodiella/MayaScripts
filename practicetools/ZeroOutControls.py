#
# Zero Out Controls by Melodi
#

# Explanation:
import maya.cmds as cmds
#imports maya commands

control_selection = cmds.ls(long=True, type="transform")
# lists select of nurbs curves controls

cmds.select(control_selection, replace=True)
# selects nurbs curves controls

# loop through those controls
for shape in control_selection:
    offset_grp = f"{ctrl}_offset_grp"

# store parent information
    transform = cmds.listRelatives(shape, parent=True)[0]

    cmds.group(empty=True, name=offset_grp)

# create a freeze/offset group

    cmds.matchTransform(offset_grp, ctrl, pos=True, rot=True, scale=False)

# Parent offset group back under original hierarchy
    cmds.parent(offset_grp, transform)
# selects attributes on control

# changes attributes to 0 for translate and rotate, scale stays 1, 1, 1

    cmds.setAttr(ctrl + ".translateX", 0)
    cmds.setAttr(ctrl + ".translateY", 0)
    cmds.setAttr(ctrl + ".translateZ", 0)

    cmds.setAttr(ctrl + ".rotateX", 0)
    cmds.setAttr(ctrl + ".rotateY", 0)
    cmds.setAttr(ctrl + ".rotateZ", 0)

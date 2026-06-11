"""
Object Renamer by Melodi
"""
from maya import cmds

SUFFIXES = {
    "mesh": "geo",
    "joint": "jnt",
    "camera": None,
    "ambientLight": "lgt"
}

DEFAULT_SUFFIX = "grp"

def rename(selection=False):
    objects = cmds.ls(selection=selection, dag=True, long=True) or []

    if selection and not objects:
        raise RuntimeError("You don't have anything selected!")

    objects.sort(key=len, reverse=True)

    renamed_objects = []

    for obj in objects:
        shortName = obj.split("|")[-1]

        children = cmds.listRelatives(obj, children=True, fullPath=True) or []

        if len(children) == 1:
            child = children[0]
            objType = cmds.objectType(child)
        else:
            objType = cmds.objectType(obj)

        suffix = SUFFIXES.get(objType, DEFAULT_SUFFIX)

        if suffix is None:
            print("Skipping %s" % obj)
            continue

        if shortName.endswith("_" + suffix):
            renamed_objects.append(obj)
            continue

        newName = "%s_%s" % (shortName, suffix)
        renamed = cmds.rename(obj, newName)
        renamed_objects.append(renamed)

    return renamed_objects

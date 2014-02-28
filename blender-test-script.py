import sys
import os
for p in (
        "/Users/linus/Documents/Lessons/ISN/bac-lsystems",
        "... put the full path to your git checkout of the repo here"):
    if os.path.isdir(p):
        sys.path.append(p)
        break

import demo
import lsys
import lsys.render.blender_renderer as bmr
import imp
imp.reload(lsys)
imp.reload(bmr)

s = demo.DemoSystem(renderer=bmr.BlenderMeshRenderer())

s.construct(depth=10)
s.render()

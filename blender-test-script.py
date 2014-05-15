import sys
import os
for p in (
            "/Users/linus/Documents/Lessons/ISN/bac-lsystems",
            "C:/Users/Dirk Duckson/Documents/Interactive Art/Learning/L-systems ISN"
         ):
    if os.path.isdir(p):
        sys.path.append(p)
        break

import lsys
import lsys.render.blender_renderer as bmr
import lsys.example.fern as fern
import imp
imp.reload(fern)
imp.reload(lsys)
imp.reload(bmr)

s = fern.FernDrawer(renderer=bmr.BlenderMeshRenderer(scale=0.1), depth=7)

s.draw()

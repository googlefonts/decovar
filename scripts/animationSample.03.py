import os
import subprocess
import shutil
import random
from drawbotlab.vfont import VFInstance
from drawbotlab.math import lerp, norm

base = os.path.split(os.path.split(__file__)[0])[0]
srcPath = os.path.join(base, 'sources/2-build/Decovar-VF.ttf')

transitions = [
    (
     {
    'sklA': 1000,
    'sklB': 0,
    'trmE': 0,
    'trmK': 1000,
    'trmL': 0,
    },
    {
    'sklA': 0,
    'sklB': 0,
    'trmE': 0,
    'trmK': 0,
    'trmL': 0,

    },
    (1, 1, 0),
    (1, 0, 0)
    ),
    
    ########
    
    (
     {
    'sklA': 0,
    'sklB': 0,
    'trmE': 0,
    'trmK': 0,
    'trmL': 0,
    
    },
    {
    'sklA': 0,
    'sklB': 0,
    'trmE': 1000,
    'trmK': 0,
    'trmL': 0,
    },
    (1, 0, 0),
    (1, 1, 0),
    ),
     
    
    ########
    (
     {
    'sklA': 0,
    'sklB': 0,
    'trmE': 1000,
    'trmK': 0,
    'trmL': 0,
    
    },
    {

    'sklA': 0,
    'sklB': 1000,
    'trmE': 0,
    'trmK': 0,
    'trmL': 1000,

    },
    (1, 1, 0),
    (1, 0, 0)
    ),
     
     
    ########
    (
     {
    'sklA': 0,
    'sklB': 1000,
    'trmE': 0,
    'trmK': 0,
    'trmL': 1000,
    },
    {
    'sklA': 1000,
    'sklB': 0,
    'trmE': 0,
    'trmK': 1000,
    'trmL': 0,

    },
    (1, 0, 0),
    (1, 1, 0)
    ),
     
    
    ]

frames = 30

for transition in transitions:
    locationMin, locationMax, colorMin, colorMax = transition
    for i in range(frames+1):
        progress = lerp(0, frames, i)
        print progress,
        thisLocation = {}
        for axis in locationMin.keys():
            try:
                thisLocation[axis] = norm(progress, locationMin.get(axis) or 0, locationMax.get(axis) or 0)
            except:
                thisLocation[axis] = 0
        print thisLocation
        vfi = VFInstance(srcPath, thisLocation)

        try:
            thisColorR = norm(progress, colorMin[0], colorMax[0])
        except:
            thisColorR = 0
        try:
            thisColorG = norm(progress, colorMin[1], colorMax[1])
        except:
            thisColorG = 0
        try:
            thisColorB = norm(progress, colorMin[2], colorMax[2])
        except:
            thisColorB = 0
     
        newPage(1198, 1000)
        frameDuration(.1)
    
        fill(thisColorR, thisColorG, thisColorB)
        rect(0, 0, width(), height())

        fill(1)

        installFont(vfi.getPath())
        fontSize(300)
        lineHeight(250)
        font(vfi.getName())
        textBox('TYPO\nVARIA\nTIONS', (0, -150, width(), height()), align="center")
        uninstallFont(vfi.getPath())
        
        vfi.remove()

saveImage(
    [
    os.path.join(base, 'documentation/sample.mov'), 
    os.path.join(base, 'documentation/sample.gif')
    ]
    )
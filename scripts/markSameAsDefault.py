"""
A script that compares glyphs to the default style, and marks them if the point digests are identical. Uses robofab.
"""

import os
from robofab.pens.digestPen import DigestPointPen

base = os.path.split(os.path.split(__file__)[0])[0]
masterPath = os.path.join(base, 'sources/1-drawing')

paths = []

for filename in os.listdir(masterPath):
    if filename.endswith('.ufo'):
        paths.append(os.path.join(masterPath, filename))

srcPath = os.path.join(masterPath, 'Decovar-Regular24.ufo')
src = OpenFont(srcPath, showUI=False)

for path in paths:
    f = OpenFont(path, showUI=False)
    for g in f:
        if src.has_key(g.name):

            destPen = DigestPointPen()
            g.drawPoints(destPen)
            destDigest = destPen.getDigest()

            srcPen = DigestPointPen()
            src[g.name].drawPoints(srcPen)
            srcDigest = srcPen.getDigest()
            
            if destDigest == srcDigest:
                g.mark = (0, .5, 1, .5)
    f.save()
    f.close()
print 'done'
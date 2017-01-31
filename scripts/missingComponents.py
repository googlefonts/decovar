# report any missing components

import os

base = os.path.split(os.path.split(__file__)[0])[0]
masterPath = os.path.join(base, 'sources/1-drawing')

paths = []
for filename in os.listdir(masterPath):
    if filename.endswith('.ufo'):
        paths.append(os.path.join(masterPath, filename))


for path in paths:
    f = OpenFont(path, showUI=False)
    for g in f:
        for c in g.components:
            if c.baseGlyph not in f.keys():
                g.removeComponent(c)
                print 'missing', c.baseGlyph, 'in', g.name, f.path
    f.save()
print 'done'
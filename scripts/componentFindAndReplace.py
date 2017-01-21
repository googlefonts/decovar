import os
base = os.path.split(os.path.split(__file__)[0])[0]
masterPath = os.path.join(base, 'sources/1-drawing')

componentFind = 'BaseElement2'
componentReplace = 'BaseElementV2'

for filename in os.listdir(masterPath):
    if filename.endswith('.ufo'):

        f = OpenFont(path, showUI=False)
        for g in f:
            for c in g.components:
                if c.baseGlyph == componentFind:
                    c.baseGlyph = componentReplace
        f.save()
print 'done'
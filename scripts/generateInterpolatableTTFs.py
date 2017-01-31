# a robofont script for generating interpolatable TTFs

import os
base = os.path.split(os.path.split(__file__)[0])[0]
masterPath = os.path.join(base, 'sources/1-drawing')

for filename in os.listdir(masterPath):
    if filename.endswith('.ufo'):
        path = os.path.join(masterPath, filename)
        f= OpenFont(path, showUI=False)
        f.generate(path.replace('.ufo', '.ttf'), 'ttf', decompose=True, checkOutlines=False, autohint=False)
        f.close()
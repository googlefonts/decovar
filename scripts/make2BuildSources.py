# copy all sources to build folder, decompose

import shutil
import os

base = os.path.split(os.path.split(__file__)[0])[0]
drawingPath = os.path.join(base, 'sources/1-drawing')
buildPath = os.path.join(base, 'sources/2-build')




for filename in os.listdir(buildPath):
    if filename.endswith('.ufo'):
        shutil.rmtree(os.path.join(buildPath, filename))
        

for filename in os.listdir(drawingPath):
    if filename.endswith('.ufo'):
        shutil.copytree(os.path.join(drawingPath, filename), os.path.join(buildPath, filename))
        
        f = OpenFont(os.path.join(buildPath, filename), showUI=False)            
        for g in f:
            g.decompose()
        f.save()
        



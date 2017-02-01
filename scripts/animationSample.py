import os
import subprocess
import shutil
import random
from fontTools.ttLib import TTFont
import uuid

pathToFontToolsMutator = '/Users/david/Documents/Tools/fonttools/Lib/fontTools/varLib/mutator.py'

base = os.path.split(os.path.split(__file__)[0])[0]
srcPath = os.path.join(base, 'sources/2-build/Decovar-VF.ttf')

tempDest = os.path.join(base, 'sources/2-build/Decovar-VF-instance.ttf')

tempDir = os.path.join(base, 'tmp')

if not os.path.exists(tempDir):
    os.mkdir(tempDir)

for frame in range(20):
    newPage(1200, 1000)
    frameDuration(.3)

    location = {
        'trmA': random.choice([0, 1000, 0]),
        'trmB': random.choice([0, 1000, 0]),
        'trmC': random.choice([0, 1000, 0]),
        'trmD': random.choice([0, 1000, 0]),
        'trmE': random.choice([0, 1000, 0]),
        'trmF': random.choice([0, 1000, 0]),
        'trmG': random.choice([0, 1000, 0]),
        'trmK': random.choice([0, 1000, 0]),
        'trmL': random.choice([0, 1000, 0]),

        'sklA': random.choice([0, 1000]),
        'sklB': random.choice([0, 1000]),
        'sklD': random.choice([0, 1000]),
        
        }

    cmds = ['python', pathToFontToolsMutator, srcPath]
    for k, v in location.items():
        cmds.append('%s=%s' %(k, v))
    print '---'
    print ' '.join(cmds)
    print '---'
    proc = subprocess.Popen(cmds, stdout=subprocess.PIPE)
    out = proc.communicate()[0]
    print out
    myUUID = str(uuid.uuid4())[6]
    f = TTFont(tempDest)
    f['name'].setName('Decovar'+str(myUUID), 6, 1, 0, 0) # Macintosh
    f['name'].setName('Decovar'+str(myUUID), 6, 3, 1, 0x409) # Windows
    os.remove(tempDest)
    instancePath = os.path.join(tempDir, 'temp_%s_%s.ttf' % (str(myUUID), str(frame) ))
    f.save(instancePath)
    
    fill(random.random(), random.random(), random.random(), 1)
    rect(0, 0, width(), height())

    fill(random.random(), random.random(), random.random(), 1)


    installFont(instancePath)
    fontSize(300)
    lineHeight(250)
    font('Decovar'+str(myUUID))
    textBox('WRECK\nO\nVAR', (0, -150, width(), height()), align="center")
    uninstallFont(instancePath)

shutil.rmtree(tempDir)
saveImage(os.path.join(base, 'documentation/sample.gif'))
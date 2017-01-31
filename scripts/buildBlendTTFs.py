import os
from fontTools.ttLib import TTFont
import subprocess

base = os.path.split(os.path.split(__file__)[0])[0]
srcPath = os.path.join(base, 'sources/2-build/Decovar-VF.ttf')
pathToFontToolsMutator = '/Users/david/Documents/Tools/fonttools/Lib/fontTools/varLib/mutator.py'



blendMap = {
    
    'bldA': {'sklA': 1000, 'trmK': 1000}, 
    'bldB': {'sklB': 1000, 'trmL': 1000},
    
    }

tempDest = os.path.join(base, 'sources/2-build/Decovar-VF-instance.ttf')
    
for name, location in blendMap.items():
    cmds = ['python', pathToFontToolsMutator, srcPath]
    for k, v in location.items():
        cmds.append('%s=%s' %(k, v))
    print '---'
    print ' '.join(cmds)
    print '---'
    proc = subprocess.Popen(cmds, stdout=subprocess.PIPE)
    out = proc.communicate()[0]
    print out
    destPath = os.path.join(base, 'sources/2-build/Decovar-Regular24%s.ttf' %str(name))
    f = TTFont(tempDest)
    f['name'].setName(u'Fit-Instance'+str(v), 6, 3, 1, 1033)
    os.remove(tempDest)
    f.save( destPath)

    
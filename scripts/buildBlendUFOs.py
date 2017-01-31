from mutatorMath.ufo.document import DesignSpaceDocumentReader
from mutatorMath.objects.mutator import Mutator, buildMutator, Location
from mutatorMath.ufo.instance import InstanceWriter
from mutatorMath.ufo.document import initializeLogger
import os

import mutatorMath

base = os.path.split(os.path.split(__file__)[0])[0]
buildPath = os.path.join(base, 'sources/2-build')

ds = DesignSpaceDocumentReader(os.path.join(buildPath, 'Decovar.designspace'), 2, True)
log = initializeLogger(os.path.join(buildPath, 'mutatormath.log'))

blendMap = {
    
    'bldA': {'sklA': 1000, 'trmK': 1000}, 
    'bldB': {'sklB': 1000, 'trmL': 1000}
    
    }

for name, location in blendMap.items():
    location = Location(location)
    destPath = os.path.join(buildPath, 'Decovar-Regular24'+name+'.ufo')
    u = InstanceWriter(destPath, verbose=True, logger=log)
    u.setSources(ds.sources)
    u.setLocation(location)
    totalWidth = 0
    for gname in u.getAvailableGlyphnames():
        u.addGlyph(gname)
    u.addInfo()
    u.addKerning()
    u.font.save(destPath)
        


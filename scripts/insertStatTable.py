import os
import sys
from fontTools.ttLib import TTFont, newTable
print 'inserting STAT table from external file...'
arguments = sys.argv[1:]
path = arguments[0]
f = TTFont(path)
base = os.path.split(os.path.split(__file__)[0])[0]
pathToXML = os.path.join(base, 'sources/2-build/STAT.ttx')
f['STAT'] = newTable('STAT')
f.importXML(pathToXML)
os.remove(path)
f.save(path)
import os
paths = [u"/Users/david/Desktop/workspace/FB/Decovar Axis/Decovar Axis1.0/Decovar-Regular24DB.ufo", u"/Users/david/Desktop/workspace/FB/Decovar Axis/Decovar Axis1.0/Decovar-SkeletonA24DB.ufo", u"/Users/david/Desktop/workspace/FB/Decovar Axis/Decovar Axis1.0/Decovar-SkeletonB24DB.ufo", u"/Users/david/Desktop/workspace/FB/Decovar Axis/Decovar Axis1.0/Decovar-SkeletonC24DB.ufo", u"/Users/david/Desktop/workspace/FB/Decovar Axis/Decovar Axis1.0/Decovar-TerminalA24DB.ufo", u"/Users/david/Desktop/workspace/FB/Decovar Axis/Decovar Axis1.0/Decovar-TerminalB24DB.ufo", u"/Users/david/Desktop/workspace/FB/Decovar Axis/Decovar Axis1.0/Decovar-TerminalC24DB.ufo", u"/Users/david/Desktop/workspace/FB/Decovar Axis/Decovar Axis1.0/Decovar-TerminalD24DB.ufo", u"/Users/david/Desktop/workspace/FB/Decovar Axis/Decovar Axis1.0/Decovar-TerminalE24DB.ufo", u"/Users/david/Desktop/workspace/FB/Decovar Axis/Decovar Axis1.0/Decovar-TerminalF24DB.ufo", u"/Users/david/Desktop/workspace/FB/Decovar Axis/Decovar Axis1.0/Decovar-TerminalG24DB.ufo", u"/Users/david/Desktop/workspace/FB/Decovar Axis/Decovar Axis1.0/Decovar-TerminalJ24DB.ufo"]

def getAxisName(path):
    base, fileAndExt = os.path.split(path)
    filename = os.path.splitext(fileAndExt)[0]
    axisName = filename.replace('Decovar-', '').replace('24DB', '')
    axisName = axisName.replace('Terminal', 'trm').replace('Skeleton', 'skl')
    return axisName

base = os.path.split(paths[0])[0]

axes = []
for path in paths:
    axisName = getAxisName(path)
    if axisName != 'Regular':
        axes.append(axisName)

xml = """<?xml version='1.0' encoding='utf-8'?>

<designspace format="3">

    <sources>
"""

for path in paths:
    
    axisName = getAxisName(path)
    xml += """
    
        <source filename="%s" name="master_%s">
    """ %(os.path.split(path)[1], axisName)
    
    if axisName == 'Regular':
        xml+= """
            <lib copy="1" />
            <groups copy="1" />
            <info copy="1" />
        """
    
    xml += """
        <location>"""
    
    for axis in axes:
        if axisName == axis:
            xml += """
            <!-- PRIME --><dimension name="%s" xvalue="1000" />""" %axis
        else:
            xml += """
            <dimension name="%s" xvalue="0" />""" %axis
    
    xml += """
        </location>
    </source>"""


xml += """

    </sources>
    <instances />
</designspace>

"""
for axis in axes:
    		print "'%s':  ('%s', '%s'), " %(axis,axis,axis.replace('skl', 'Skeleton ').replace('trm', 'Terminal '))
    
    
from fbits.toolbox.file import File

File.write(xml, os.path.join(base, 'Decovar.designspace'))
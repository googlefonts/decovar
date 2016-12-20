from drawbotlab.glyph import drawGlyph
import subprocess
import os
import tempfile
import shutil
from fontTools.ttLib import TTFont


interactive = False
reset = False

globalVars = globals()
def buildDrawBotVariableSlidersList(axes):
    variableSliders = []
    for axisName in sorted(axes.keys()):
        axisMin, axisMax, axisDefault = axes[axisName]
        variableSliders.append(
            dict(name=axisName, ui="Slider", 
                args=dict( 
                    # some vanilla specific 
                    # setting for a slider
                    value=axisDefault, 
                    minValue=axisMin, 
                    maxValue=axisMax,
                    ))
            )
    return variableSliders


defaultCheckbox = [
            dict(name='reset', ui="CheckBox", 
                args=dict( 
                    # some vanilla specific 
                    # setting for a slider
                    value=False, 
                    )
                )
]


base = os.path.split(os.path.split(__file__)[0])[0]
myText = 'BILLHOLDER\nBOILED BEEF\nFIDDLEDEEDEE'


srcPath = os.path.join(base, 'fonts/Decovar-VF.ttf')




axes = {'sklB': (0, 1000, 0), 'sklC': (0, 1000, 0), 'sklA': (0, 1000, 0), 'trmA': (0, 1000, 0), 'trmC': (0, 1000, 0), 'trmB': (0, 1000, 0), 'trmE': (0, 1000, 0), 'trmD': (0, 1000, 0), 'trmG': (0, 1000, 0), 'trmF': (0, 1000, 0), 'trmJ': (0, 1000, 0)}
axisNames = sorted(axes.keys())


if interactive:
    Variable(buildDrawBotVariableSlidersList(axes), globalVars)
    frames = 1
    if reset:
        for axis, values in axes.items():
            globalVars[axis] = values[2]
    
else:
    for axis, values in axes.items():
        globalVars[axis] = values[2]
    segmentFrames = 10
    frames = segmentFrames * 2 * len(axisNames)



if not interactive:
    currentAxisIndex = 0
    currentAxis = axisNames[currentAxisIndex]
    globalVars[currentAxis] = axes[currentAxis][0]
    increment = (axes[currentAxis][1] - axes[currentAxis][0]) / segmentFrames

direction = 1

fontsToRemove = []

for frame in range(frames):
    # make a new frame
    newPage(1000, 550)
    # draw a background
    fill(1)
    rect(0, 0, width(), height())
    fill(0)

    # make a location, and also fill the readout
    instanceDict = {}
    readouts = []

    for axis in axisNames:
        instanceDict[axis] = globalVars[axis]
        readouts.append( '%s: %d' %(axis, instanceDict[axis]))
    readout = ' | '.join(readouts)
    
    # build an instance font from the location
    location = instanceDict
    
    
    cmds = ['python', '/Users/david/Documents/Tools/fonttools/Lib/fontTools/varLib/mutator.py', srcPath]
    for k, v in location.items():
        cmds.append('%s=%s' %(k, v))

    proc = subprocess.Popen(cmds, stdout=subprocess.PIPE)
    out = proc.communicate()[0]
    print out

    translate(40, 20)

    # draw the readout
    font('Input Mono', 10)
    textBox(readout, (0, height()-80, width()-50, 20))

    # make it fit the height
    
    translate(0, 0)
    # draw the glyphs
    totalWidth = 0
    save()
    
    tempPath = os.path.join(base, 'fonts/Decovar-Instance%s.ttf' %str(frame))
    print tempPath
    instancePath = os.path.join(base, 'fonts/Decovar-VF-instance.ttf')
    tempttf = TTFont(instancePath)
    
    tempttf['name'].setName(u'Decovar-Instance'+str(frame), 6, 3, 1, 1033)
    tempttf.save(tempPath)
    
    font(tempPath)
    fontSize(150)
    lineHeight(125)    
    textBox(myText, (0, 0, width()*2, height()-100))
    
    #uninstallFont(instancePath)
    #os.remove(temp)
    os.remove(instancePath)
    fontsToRemove.append(tempPath)

    # increment the value for the next frame
    if not interactive:
        globalVars[currentAxis] += (increment * direction)
    
    # if we hit the halfway mark, go back to the minimum
    if frame > 0 and frame % segmentFrames == 0 and not interactive:
        direction = -1
        
    # after the direction has regressed, bump to the next axis
    if frame > 0 and frame % (segmentFrames*2) == 0 and not interactive:
        # return to default
        globalVars[currentAxis] = axes[currentAxis][2]
        # set next current axis
        currentAxisIndex += 1        
        currentAxis = axisNames[currentAxisIndex]
        globalVars[currentAxis] = axes[currentAxis][0]
        increment = (axes[currentAxis][1] - axes[currentAxis][0]) / segmentFrames
        direction = 1
        
    with open(os.path.join(base, 'status.txt'), 'w') as statusFile:
        statusFile.write('%s/%s' %(str(frame+1), str(frames)))
    
    #u.save()
if not interactive:
    saveImage(os.path.join(base, 'decovar-demo.gif'))

for path in fontsToRemove:
    os.remove(path)
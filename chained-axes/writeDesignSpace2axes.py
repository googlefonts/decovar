from designSpaceDocument import DesignSpaceDocument, SourceDescriptor, InstanceDescriptor, AxisDescriptor
import os

###

designSpacePath = "Decovar.designspace"
familyName = "Decovar"

sources = [
	dict(path="master_ufo/Decovar-Regular24.ufo", name="Decovar-Regular24.ufo", location=dict(skeleton=0, terminal=0), styleName="Regular24", familyName=familyName, copyInfo=True),
	dict(path="master_ufo/Decovar-Regular24SkelA.ufo", name="Decovar-Regular24SkelA.ufo", location=dict(skeleton=1), styleName="SkelA", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24.ufo", name="Decovar-Regular24.ufo", location=dict(skeleton=1.5), styleName="Regular24", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24SkelD2.ufo", name="Decovar-Regular24SkelD2.ufo", location=dict(skeleton=2), styleName="SkelD", familyName=familyName, copyInfo=False),
#	dict(path="master_ufo/Decovar-Regular24SkelD4.ufo", name="Decovar-Regular24SkelD4.ufo", location=dict(skeleton=3), styleName="SkelD", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24.ufo", name="Decovar-Regular24.ufo", location=dict(skeleton=2.5), styleName="Regular24", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24SkelB2.ufo", name="Decovar-Regular24SkelB2.ufo", location=dict(skeleton=3), styleName="SkelB", familyName=familyName, copyInfo=False),


	dict(path="master_ufo/Decovar-Regular24TermA.ufo", name="Decovar-Regular24TermA.ufo", location=dict(terminal=0.5), styleName="TermA", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24TermA2.ufo", name="Decovar-Regular24TermA2.ufo", location=dict(terminal=1), styleName="TermA", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24.ufo", name="Decovar-Regular24.ufo", location=dict(terminal=1.5), styleName="Regular24", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24TermB.ufo", name="Decovar-Regular24TermB.ufo", location=dict(terminal=2), styleName="TermB", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24.ufo", name="Decovar-Regular24.ufo", location=dict(terminal=2.5), styleName="Regular24", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24TermC.ufo", name="Decovar-Regular24TermC.ufo", location=dict(terminal=3), styleName="TermC", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24.ufo", name="Decovar-Regular24.ufo", location=dict(terminal=3.5), styleName="Regular24", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24TermD.ufo", name="Decovar-Regular24TermD.ufo", location=dict(terminal=4), styleName="TermD", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24.ufo", name="Decovar-Regular24.ufo", location=dict(terminal=4.5), styleName="Regular24", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24TermE.ufo", name="Decovar-Regular24TermE.ufo", location=dict(terminal=5), styleName="TermE", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24.ufo", name="Decovar-Regular24.ufo", location=dict(terminal=5.5), styleName="Regular24", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24TermF.ufo", name="Decovar-Regular24TermF.ufo", location=dict(terminal=6), styleName="TermF", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24.ufo", name="Decovar-Regular24.ufo", location=dict(terminal=6.5), styleName="Regular24", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24TermG.ufo", name="Decovar-Regular24TermG.ufo", location=dict(terminal=7), styleName="TermG", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24.ufo", name="Decovar-Regular24.ufo", location=dict(terminal=7.5), styleName="Regular24", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24TermSkelA.ufo", name="Decovar-Regular24TermSkelA.ufo", location=dict(terminal=8), styleName="TermSkelA", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24.ufo", name="Decovar-Regular24.ufo", location=dict(terminal=8.5), styleName="Regular24", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24TermSkelB.ufo", name="Decovar-Regular24TermSkelB.ufo", location=dict(terminal=9), styleName="TermSkelB", familyName=familyName, copyInfo=False),
]
axes = [
	dict(minimum=0, maximum=3, default=0, name="skeleton", tag="SKEL", labelNames={"en": "Skeleton"}, map=[]),
	dict(minimum=0, maximum=9, default=0, name="terminal", tag="TERM", labelNames={"en": "Terminal"}, map=[]),
]

instances = [
	dict(location=dict(skeleton=0, terminal=0), styleName="Regular", familyName=familyName),
	dict(location=dict(skeleton=1, terminal=8), styleName="Open", familyName=familyName),
	dict(location=dict(skeleton=3, terminal=9), styleName="Worm", familyName=familyName),
	dict(location=dict(skeleton=1, terminal=0), styleName="Checkered", familyName=familyName),
	dict(location=dict(skeleton=0, terminal=8), styleName="Checkered Reverse", familyName=familyName),
	dict(location=dict(skeleton=2, terminal=0), styleName="Stripped", familyName=familyName),
	dict(location=dict(skeleton=0, terminal=1), styleName="Rounded", familyName=familyName),
	dict(location=dict(skeleton=0, terminal=2), styleName="Flared", familyName=familyName),
	dict(location=dict(skeleton=1, terminal=2), styleName="Flared Open", familyName=familyName),
	dict(location=dict(skeleton=0, terminal=3), styleName="Rounded Slab", familyName=familyName),
	dict(location=dict(skeleton=0, terminal=4), styleName="Sheared", familyName=familyName),
	dict(location=dict(skeleton=0, terminal=5), styleName="Bifurcated", familyName=familyName),
	dict(location=dict(skeleton=1.25, terminal=8.25), styleName="Inline", familyName=familyName),
	dict(location=dict(skeleton=0, terminal=7), styleName="Slab", familyName=familyName),
	dict(location=dict(skeleton=1.25, terminal=7), styleName="Slab Inline", familyName=familyName),
	# Contrast
	# Fancy
	# Mayhem
]

#for source in sources:
#	instances.append(dict(location=source["location"], styleName=source["styleName"], familyName=source["familyName"]))

### 

doc = DesignSpaceDocument()

for source in sources:
	s = SourceDescriptor()
	s.path = source["path"]
	s.name = source["name"]
	s.copyInfo = source["copyInfo"]
	s.location = source["location"]
	s.familyName = source["familyName"]
	s.styleName = source["styleName"]
	doc.addSource(s)

for instance in instances:
	i = InstanceDescriptor()
	i.location = instance["location"]
	i.familyName = instance["familyName"]
	i.styleName = instance["styleName"]
	doc.addInstance(i)

for axis in axes:
	a = AxisDescriptor()
	a.minimum = axis["minimum"]
	a.maximum = axis["maximum"]
	a.default = axis["default"]
	a.name = axis["name"]
	a.tag = axis["tag"]
	for languageCode, labelName in axis["labelNames"].items():
		a.labelNames[languageCode] = labelName
	a.map = axis["map"]
	doc.addAxis(a)

#doc.checkAxes()

#doc.checkDefault()

doc.write(designSpacePath)

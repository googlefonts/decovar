from designSpaceDocument import DesignSpaceDocument, SourceDescriptor, InstanceDescriptor, AxisDescriptor
import os

###

designSpacePath = "Decovar.designspace"
familyName = "Decovar"

sources = [
	dict(path="master_ufo/Decovar-Regular24.ufo", name="Decovar-Regular24.ufo", location=dict(inline=0, serif=0, terminal=0, weight=0, flower=0), styleName="Regular24", familyName=familyName, copyInfo=True),
	dict(path="master_ufo/Decovar-Regular24bldA.ufo", name="Decovar-Regular24bldA.ufo", location=dict(inline=1), styleName="BlendA", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24.ufo", name="Decovar-Regular24.ufo", location=dict(inline=1.5), styleName="Regular24", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24SkelA.ufo", name="Decovar-Regular24SkelA.ufo", location=dict(inline=2), styleName="SkelA", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24.ufo", name="Decovar-Regular24.ufo", location=dict(inline=2.5), styleName="Regular24", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24TermSkelA.ufo", name="Decovar-Regular24TermSkelA.ufo", location=dict(inline=3), styleName="TermSkelA", familyName=familyName, copyInfo=False),
	
	dict(path="master_ufo/Decovar-Regular24bldB.ufo", name="Decovar-Regular24bldB.ufo", location=dict(flower=1), styleName="BlendB", familyName=familyName, copyInfo=False),
	
	dict(path="master_ufo/Decovar-Regular24TermB.ufo", name="Decovar-Regular24TermB.ufo", location=dict(serif=1), styleName="TermB", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24.ufo", name="Decovar-Regular24.ufo", location=dict(serif=1.5), styleName="Regular24", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24TermC.ufo", name="Decovar-Regular24TermC.ufo", location=dict(serif=2), styleName="TermC", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24.ufo", name="Decovar-Regular24.ufo", location=dict(serif=2.5), styleName="Regular24", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24TermG.ufo", name="Decovar-Regular24TermG.ufo", location=dict(serif=3), styleName="TermG", familyName=familyName, copyInfo=False),

	dict(path="master_ufo/Decovar-Regular24TermA.ufo", name="Decovar-Regular24TermA.ufo", location=dict(terminal=1), styleName="TermA", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24.ufo", name="Decovar-Regular24.ufo", location=dict(terminal=1.5), styleName="Regular24", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24TermD.ufo", name="Decovar-Regular24TermD.ufo", location=dict(terminal=2), styleName="TermD", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24.ufo", name="Decovar-Regular24.ufo", location=dict(terminal=2.5), styleName="Regular24", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24TermE.ufo", name="Decovar-Regular24TermE.ufo", location=dict(terminal=3), styleName="TermE", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24.ufo", name="Decovar-Regular24.ufo", location=dict(terminal=3.5), styleName="Regular24", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Decovar-Regular24TermF.ufo", name="Decovar-Regular24TermF.ufo", location=dict(terminal=4), styleName="TermF", familyName=familyName, copyInfo=False),
	
	dict(path="master_ufo/Decovar-Regular24WeightMax2.ufo", name="Decovar-Regular24WeightMax2.ufo", location=dict(weight=1), styleName="WeightMax2", familyName=familyName, copyInfo=False),

	#Decovar-Regular24TermSkelA.ufo
	#Decovar-Regular24TermSkelB.ufo
	
]
axes = [
	dict(minimum=0, maximum=3, default=0, name="inline", tag="inli", labelNames={"en": "Inline"}, map=[]),
	dict(minimum=0, maximum=1, default=0, name="flower", tag="flow", labelNames={"en": "Flower"}, map=[]),
	dict(minimum=0, maximum=3, default=0, name="serif", tag="srif", labelNames={"en": "Serif"}, map=[]),
	dict(minimum=0, maximum=4, default=0, name="terminal", tag="term", labelNames={"en": "Terminal"}, map=[]),
	dict(minimum=0, maximum=1, default=0, name="weight", tag="wght", labelNames={"en": "Weight"}, map=[]),
]

instances = [
	dict(location=dict(inline=1), styleName="Inline", familyName=familyName),
	
	dict(location=dict(serif=1), styleName="Serif1", familyName=familyName),
	dict(location=dict(serif=2), styleName="Serif2", familyName=familyName),
	dict(location=dict(serif=3), styleName="Serif4", familyName=familyName),
	
	dict(location=dict(terminal=1), styleName="Term1", familyName=familyName),
	dict(location=dict(terminal=2), styleName="Term2", familyName=familyName),
	dict(location=dict(terminal=3), styleName="Term3", familyName=familyName),
	dict(location=dict(terminal=4), styleName="Term4", familyName=familyName),

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

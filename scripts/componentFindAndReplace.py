f = CurrentFont()

componentFind = 'WaistElement'
componentReplace = 'WaistElement2'

for g in f:
    for c in g.components:
        if c.baseGlyph == componentFind:
            c.baseGlyph = componentReplace
print 'done'
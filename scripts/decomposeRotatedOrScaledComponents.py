f = CurrentFont()

#defaults
xyd = 1
yyd = 0
xxd = 0
yxd = 1

for g in f:
    for c in g.components:
        xy, yy, xx, yx, x, y = c.transformation
        if xy != xyd or yy != yyd or xx != xxd or yx != yxd:
            print '\t', 'Decomposing', c.baseGlyph, 'in', g.name
            g.prepareUndo()
            c.decompose()
            g.performUndo()
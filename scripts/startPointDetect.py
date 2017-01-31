# in CurrentGlyph(), set start points to bottom-most, left-most


def getLeftMostBottomMost(c):
    a = []
    for b in c.bPoints:
        a.append(b.anchor)
    a.sort()
    for b in c.bPoints:
        if b.anchor == a[0]:
            return b

def getBottomMostLeftMost(c):
    a = []
    for b in c.bPoints:
        a.append((b.anchor[1], b.anchor[0]))
    a.sort()
    for b in c.bPoints:
        if (b.anchor[1], b.anchor[0]) == a[0]:
            return b

if True:
    if True:
        g = CurrentGlyph()
        g.prepareUndo()
        g.autoContourOrder()
        for ci, c in enumerate(g.contours):
            if not c.clockwise:
                c.reverseContour()
            bmlm = getBottomMostLeftMost(c)
            newStart = None
            for i, s in enumerate(c.segments):
                if (s.onCurve.x, s.onCurve.y) == bmlm.anchor:
                    newStart = i
                    print g.name, bmlm.anchor, newStart
            try:
                c.setStartSegment(newStart+1)
            except:
                c.setStartSegment(0)
        g.performUndo()
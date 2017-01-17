for path in [u"/Users/david/Desktop/workspace/FB/fb-Decovar/sources/1-drawing/Decovar-Regular24.ufo", u"/Users/david/Desktop/workspace/FB/fb-Decovar/sources/1-drawing/Decovar-Regular24SkelD2.ufo", u"/Users/david/Desktop/workspace/FB/fb-Decovar/sources/1-drawing/Decovar-Regular24SkelD4.ufo", u"/Users/david/Desktop/workspace/FB/fb-Decovar/sources/1-drawing/Decovar-Regular24TermA.ufo", u"/Users/david/Desktop/workspace/FB/fb-Decovar/sources/1-drawing/Decovar-Regular24TermA2.ufo", u"/Users/david/Desktop/workspace/FB/fb-Decovar/sources/1-drawing/Decovar-Regular24TermB.ufo", u"/Users/david/Desktop/workspace/FB/fb-Decovar/sources/1-drawing/Decovar-Regular24TermC.ufo", u"/Users/david/Desktop/workspace/FB/fb-Decovar/sources/1-drawing/Decovar-Regular24TermD.ufo"]:
    f = OpenFont(path, showUI=False)
    for g in f:
        for c in g.components:
            if c.baseGlyph not in f.keys():
                g.removeComponent(c)
                print 'missing', c.baseGlyph, 'in', g.name, f.path
    f.save()
print 'done'
from robofab.pens.digestPen import DigestPointPen


src = OpenFont(u"/Users/david/Desktop/workspace/FB/Decovar Axis/Decovar Axis1.0_sub/Decovar-Regular24DB.ufo", showUI=False)

for path in [u"/Users/david/Desktop/workspace/FB/Decovar Axis/Decovar Axis1.0_sub/Decovar-SkeletonA24DB.ufo", u"/Users/david/Desktop/workspace/FB/Decovar Axis/Decovar Axis1.0_sub/Decovar-SkeletonB24DB.ufo", u"/Users/david/Desktop/workspace/FB/Decovar Axis/Decovar Axis1.0_sub/Decovar-SkeletonC24DB.ufo", u"/Users/david/Desktop/workspace/FB/Decovar Axis/Decovar Axis1.0_sub/Decovar-TerminalA24DB.ufo", u"/Users/david/Desktop/workspace/FB/Decovar Axis/Decovar Axis1.0_sub/Decovar-TerminalB24DB.ufo", u"/Users/david/Desktop/workspace/FB/Decovar Axis/Decovar Axis1.0_sub/Decovar-TerminalC24DB.ufo", u"/Users/david/Desktop/workspace/FB/Decovar Axis/Decovar Axis1.0_sub/Decovar-TerminalD24DB.ufo", u"/Users/david/Desktop/workspace/FB/Decovar Axis/Decovar Axis1.0_sub/Decovar-TerminalE24DB.ufo", u"/Users/david/Desktop/workspace/FB/Decovar Axis/Decovar Axis1.0_sub/Decovar-TerminalF24DB.ufo", u"/Users/david/Desktop/workspace/FB/Decovar Axis/Decovar Axis1.0_sub/Decovar-TerminalG24DB.ufo", u"/Users/david/Desktop/workspace/FB/Decovar Axis/Decovar Axis1.0_sub/Decovar-TerminalJ24DB.ufo"]:
    f = OpenFont(path, showUI=False)
    for g in f:
        if src.has_key(g.name):

            destPen = DigestPointPen()
            g.drawPoints(destPen)
            destDigest = destPen.getDigest()

            srcPen = DigestPointPen()
            src[g.name].drawPoints(srcPen)
            srcDigest = srcPen.getDigest()
            
            if destDigest == srcDigest:
                g.mark = (0, .5, 1, .5)
    f.save()
    f.close()
print 'done'
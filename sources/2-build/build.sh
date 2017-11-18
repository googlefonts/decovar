# requires fontmake and fonttools varlib

# use fontmake to generate variable font
fontmake -o variable -m DecovarAlpha.designspace --no-production-names

# insert STAT table (temporary)
python ../../scripts/insertStatTable.py variable_ttf/DecovarAlpha-VF.ttf

# move to main /fonts folder
mv variable_ttf/DecovarAlpha-VF.ttf ../../fonts/DecovarAlpha-VF.ttf

# generate subsetted version
pyftsubset ../../fonts/DecovarAlpha-VF.ttf --glyphs=A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,space
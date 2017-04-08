# DECOVAR

A variable decorative sans by David Berlow.

![Examples of Decovar](https://raw.githubusercontent.com/TypeNetwork/fb-Decovar/master/documentation/decovar-samples.png)

The [documentation](documentation/) contains a description of the project and typographic contents of the repo.

The [fonts](fonts/) folder of each version contains the FontName-Variations.ttf file, the Variations Font.

The [sources](sources/) folder contains the fonts with axis data in their names, used to create the Variations Font.

![Screenshot of Decovar in RoboFont](https://raw.githubusercontent.com/TypeNetwork/fb-Decovar/master/documentation/decovar-screenshot.png)

## Generating

The Decovar variable font was created with RoboFont and generated using fontTools.

To generate the correct name table, I have customized the `standard_axis_map` dictionary in `fontTools/varLib/__init__.py` with the following entries. Hopefully in future versions of fontTools this will be pulled from `Decovar.designspace` instead.

```
'WMX2':  ('wght', 'Weight'), 
'BLDA':  ('INLN', 'Inline'), 
'BLDB':  ('WORM', 'Worm'), 
'SKLA':  ('SINL', 'Inline Skeleton'), 
'SKLB':  ('SWRM', 'Worm Skeleton'), 
'SKLD':  ('SSTR', 'Stripes'),
'TRMA':  ('TRND', 'Rounded'), 
'TRMD':  ('TSHR', 'Sheared'), 
'TRMK':  ('TINL', 'Inline Terminal'), 
'TRMF':  ('TOIL', 'Open Inline Terminal'), 
'TRML':  ('TWRM', 'Worm Terminal'), 
'TRMB':  ('TFLR', 'Flared'), 
'TRME':  ('TBIF', 'Bifurcated'),
'TRMG':  ('TSLB', 'Slab'), 
'TRMC':  ('TRSB', 'Rounded Slab'), 
```

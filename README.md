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
'sklA':  ('sklA', 'Skeleton A'), 
'sklB':  ('sklB', 'Skeleton B'), 
'sklC':  ('sklC', 'Skeleton C'), 
'sklD':  ('sklD', 'Skeleton D'), 
'trmA':  ('trmA', 'Terminal A'), 
'trmB':  ('trmB', 'Terminal B'), 
'trmC':  ('trmC', 'Terminal C'), 
'trmD':  ('trmD', 'Terminal D'), 
'trmE':  ('trmE', 'Terminal E'), 
'trmF':  ('trmF', 'Terminal F'), 
'trmG':  ('trmG', 'Terminal G'), 
'trmJ':  ('trmJ', 'Terminal J'), 
'trmK':  ('trmK', 'Terminal K'), 
'trmL':  ('trmL', 'Terminal L'), 
'wmx2':  ('wmx2', 'Weight Max 2'), 
'bldA':  ('bldA', 'Blend A'), 
'bldB':  ('bldB', 'Blend B'), 
```
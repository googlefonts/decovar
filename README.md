# DECOVAR

A variable decorative sans by David Berlow.

![Examples of Decovar](https://raw.githubusercontent.com/TypeNetwork/fb-Decovar/master/documentation/decovar-samples.png)

The [documentation](documentation/) contains a description of the project and typographic contents of the repo.

The [fonts](fonts/) folder contains the DecovarAlpha-VF.ttf file, the variable font.

The [sources](sources/) folder contains the fonts with axis data in their names, used to create the Variations Font.

![Screenshot of Decovar in RoboFont](https://raw.githubusercontent.com/TypeNetwork/fb-Decovar/master/documentation/decovar-screenshot.png)

## Generating

The Decovar variable font was created with RoboFont and is generated using [fontmake](https://github.com/googlei18n/fontmake). A build script `build.sh` is included that will build the variable font using fontmake, copy it to the `/fonts` folder, and offer a subsetted version.

```
$ cd sources/2-build
$ bash build.sh
```
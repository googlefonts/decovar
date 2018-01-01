# DECOVAR

A variable decorative sans by David Berlow.

![Examples of Decovar](https://raw.githubusercontent.com/TypeNetwork/fb-Decovar/master/documentation/decovar-samples.png)

The [documentation](documentation/) contains a description of the project and typographic contents of the repo.

The [fonts](fonts/) folder contains the DecovarAlpha-VF.ttf file, the variable font.

The [sources](sources/) folder contains the fonts with axis data in their names, used to create the Variations Font.

![Screenshot of Decovar in RoboFont](https://raw.githubusercontent.com/TypeNetwork/fb-Decovar/master/documentation/decovar-screenshot.png)

## Axes

Each of Decovar’s axes has a default value of 0 and a maximum value of 1000, and are defined in the [designspace file](https://github.com/TypeNetwork/fb-Decovar/blob/master/sources/2-build/DecovarAlpha.designspace). Currently, Decovar’s axes (and their four letter tags) are as follows:

* BLDA: Inline
* BLDB: Worm
* WMX2: Weight
* SKLA: Inline Skeleton
* SKLB: Worm Skeleton
* SKLD: Stripes
* TRMA: Rounded
* TRMB: Flared
* TRMC: Rounded Slab
* TRMD: Sheared
* TRME: Bifurcated
* TRMF: Open Inline Terminal
* TRMG: Slab
* TRMK: Inline Terminal
* TRML: Worm Terminal

You can implement them in CSS like this:

```
font-variation-settings: "SKLA" 1000, "TRMG" 750;
```

## Generating

The Decovar variable font was created with RoboFont and is generated using [fontmake](https://github.com/googlei18n/fontmake). A build script `build.sh` is included that will build the variable font using fontmake, copy it to the `/fonts` folder, and offer a subsetted version.

```
$ cd sources/2-build
$ bash build.sh
```

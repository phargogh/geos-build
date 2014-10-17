wget http://download.osgeo.org/geos/geos-3.4.2.tar.bz2
tar -xvjf geos*.tar.bz2
cd geos-3.4.2
./configure --prefix=/Users/jdouglass/workspace/geos-build/geos-3.4.2/_bin
make

# where do the SO libs live?
# they appear to live in _bin/lib/ as *.dylib, on mac OSX
# on linux, these will be *.so
# on windows, (after following these instructions: http://www.gaia-gis.it/spatialite-2.4.0/mingw_how_to.html#libgeos), there will be a geos_c.dll.


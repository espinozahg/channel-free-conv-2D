#!/bin/bash

# echo $SHELL 

# ubuntu install inkscape
# apt search inkscape
# sudo apt install inkscape

# ubuntu install graphicsmagick
# apt search graphicsmagick
# sudo apt install graphicsmagick

# 2025: 1.2.2
# inkscape --version

#export LIBGL_ALWAYS_SOFTWARE=1

inkscape --export-type="pdf" --export-latex --export-filename="Tprofile" temperature_profiles_comp.svg
inkscape --export-type="png" --export-dpi=300 --export-filename="Tprofile" temperature_profiles_comp.svg

inkscape --export-type="pdf" --export-latex --export-filename="Vprofile" velocity_profiles_comp.svg
inkscape --export-type="png" --export-dpi=300 --export-filename="Vprofile" velocity_profiles_comp.svg

#inkscape --export-type="pdf" --export-latex --export-filename="pvsz" pressure_drop.svg
#inkscape --export-type="pdf" --export-latex --export-filename="dpdzvsz" pressure_drop-dpdz.svg
#inkscape --export-type="pdf" --export-latex --export-filename="perfilx" velocity_profile.svg
#inkscape --export-type="pdf" --export-latex --export-filename="perfild" velocity_profileXY-dist.svg
#inkscape --export-type="pdf" --export-latex --export-filename="mallaxy" mallaxy.svg
#inkscape --export-type="pdf" --export-latex --export-filename="mallazy" mallazy.svg


# queda de 1875 x 1250 que se ve bien
#inkscape --export-type="png" --export-dpi=300 --export-filename="pvsz" pressure_drop.svg
#inkscape --export-type="png" --export-dpi=300 --export-filename="dpdzvsz" pressure_drop-dpdz.svg
inkscape --export-type="png" --export-dpi=300 --export-filename="perfilx" velocity_profile.svg
#inkscape --export-type="png" --export-dpi=300 --export-filename="perfild" velocity_profileXY-dist.svg
#inkscape --export-type="png" --export-dpi=300 --export-filename="mallaxy" mallaxy.svg
#inkscape --export-type="png" --export-dpi=300 --export-filename="mallazy" mallazy.svg

#gm convert pvsz.png pvsz.tiff
#gm convert dpdzvsz.png dpdzvsz.tiff
gm convert perfilx.png perfilx.tiff
#gm convert perfild.png perfild.tiff

#inkscape --export-type="png" --export-dpi=300 --export-filename="bc" bc.svg
#inkscape --export-type="png" --export-dpi=300 --export-filename="geometry" geometry.svg

#gm convert bc.png bc.tiff
#gm convert geometry.png geometry.tiff


#gm convert mallaxy.png mallaxy.tiff
#gm convert mallazy.png mallazy.tiff

#--export-width=

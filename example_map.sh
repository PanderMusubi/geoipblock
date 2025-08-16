#!/usr/bin/env sh
set -e

wget -N https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip
unzip -o ne_110m_admin_0_countries.zip
./example_map.py
convert example_map.png -trim +repage example_map.png


#!/usr/bin/env python3
"""Generate example world map for blocking countries."""

import geopandas as gpd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Load Natural Earth data (stand-in for OSM country polygons)
    world = gpd.read_file('ne_110m_admin_0_countries.shp')

    # Fix invalid geometries (avoids vertical artifacts)
    world['geometry'] = world['geometry'].buffer(0)

    # Drop Antarctica to avoid projection issues
    world = world[~world['NAME'].str.contains('Antarctica')]

    # Mark highlight countries
    highlight_countries = ['AF', 'BY', 'CF', 'CN', 'CD', 'HT', 'HK', 'IL',
                           'IR', 'MM', 'MO', 'KP', 'LY', 'RU', 'SD', 'SO',
                           'SS', 'SY', 'VE', 'YE', 'ZW']
    print(','.join(highlight_countries))
    world['highlight'] = world['ISO_A2'].isin(highlight_countries)

    # Plot
    fig, ax = plt.subplots(figsize=(1920/100, 1080/100), dpi=100)

    # Background color
    fig.patch.set_facecolor('lightblue')
    ax.set_facecolor('lightblue')

    # Use Mercator projection
    world = world.to_crs(epsg=3857)

    # Non-highlighted countries
    world[~world['highlight']].plot(ax=ax, color='lightgrey',
                                    edgecolor='black', linewidth=0.5)
    # Highlight countries
    world[world['highlight']].plot(ax=ax, color='darkred',
                                   edgecolor='black', linewidth=0.5)

    ax.axis('off')
    plt.tight_layout()
    plt.savefig('example_map.png', dpi=100)

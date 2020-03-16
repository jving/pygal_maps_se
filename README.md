# Pygal_maps_se

This branch adds colormap-capabilities to the map. This should probably be in the superclass but added it to the swedish map for quickness of development.


- [Pyga_maps_sel](#pygal_maps_se)
    - [Description](#description)
    - [Installation](#installation)
    - [Contribute](#contribute)
    - [Example](#example)
    - [License](#license)

## Description

**pygal_maps_se** is map library for pygal that adds a swedish map.


Find out more about pygal on [www.pygal.org](http://www.pygal.org).

### Colormap-branch
This is a branch of the swedish map that gives the Lan-map its own _plot-function that allows for a smoot scaling colormap based on value.


## Installation

As simple as:

```
    $ pip install pygal_maps_se
```


## Example

```
chart = pygal.maps.se.Lan(width=500,height=700)
chart.add('Good places', ['H','BD'])
chart.render()
```

### Example with colormap
```
data = {
    'AB': 207,  # Stockholm
    'AC': 4,    # Västerbotten
    'BD': 2,    # Norrbotten
    'C': 8,     # Uppsala
    'D': 0,     # Södermanland
    'E': 1,     # Östergötland
    'F': 12,    # Jönköping
    'G': 17,    # Kronoberg
    'H': 2,     # Kalmar
    'I': 300,   # Gotland
    'K': 1,     # Blekinge
    'M': 60,    # Skåne
    'N': 8,     # Halland
    'O': 70,    # Västra götaland
    'S': 25,    # Värmland
    'T': 5,     # Örebro
    'U': 0,     # Västmanland
    'W': 1,     # Dalarna
    'X': 16,    # Gävleborg
    'Y': 6,     # Västernorrland
    'Z': 1,     # Jämtland
}

chart = pygal.maps.se.Lan(height=750,width=350,show_legend=False)
chart.use_cmap = True
chart.cmap = {0: (255,255,255), 1:(0,255,0),10:(0,0,255),50:(150,0,255),300:(255,16,16)}
chart.title = "Stenar per län"
chart.add("colormap",data)

chart.render_to_file('cmap.svg')
```


## Contribute

You are welcomed to fork the project and make pull requests.
Be sure to create a branch for each feature.



## License

Copyright © 2020 Jving
LGPLv3:

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

# -*- coding: utf-8 -*-
# This file is part of pygal
#
# A python svg graph plotting library
# Copyright © 2012-2015 Kozea, Serge Droz
#
# This library is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pygal. If not, see <http://www.gnu.org/licenses/>.
"""
Swedish map, län, vägregioner & kommuner

"""

from __future__ import division
from importlib.resources import files
from pygal.graph.map import BaseMap
#from pygal._compat import u
import os
import json


LAN = {
    'AB': "Stockholm",
    'C': "Uppsala",
    'D': "Södermanland",
    'E': "Östergötland",
    'F': "Jönköping",
    'G': "Kronoberg",
    'H': "Kalmar",
    'I': "Gotland",
    'K': "Blekinge",
    'M': "Skåne",
    'N': "Halland",
    'O': "Västra götaland",
    'S': "Värmland",
    'T': "Örebro",
    'U': "Västmanland",
    'X': "Gävleborg",
    'Y': "Västernorrland",
    'AC': "Västerbotten",
    'Z': "Jämtland",
    'BD': "Nottbotten",
    'W': "Dalarna",
}

REGIONER = {
    "Stockholm": "Stockholm",
    "Sydost": "Sydost",
    "Skane": "Skane",
    "Vast": "Vast",
    "Mitt": "Mitt",
    "Norr": "Norr",
}

kommun_dict_path = files("pygal_maps_se").joinpath('kommun_dict.json')
with open(kommun_dict_path,'r') as file:

    KOMMUNER = json.load(file)


with open(os.path.join(
        os.path.dirname(__file__),
        'se.lan.svg')) as file:
    LAN_MAP = file.read()

with open(os.path.join(
        os.path.dirname(__file__),
        'se.kommuner.svg')) as file:
    KOMMUN_MAP = file.read()


class Lan(BaseMap):
    """Swedish Län map"""
    x_labels = list(LAN.keys())
    area_names = LAN
    area_prefix = 's'
    kind = 'lan'
    svg_map = LAN_MAP

class VagRegion(BaseMap):
    """ Swedish Vägregion map """
    x_labels = list(REGIONER.keys())
    area_names = REGIONER
    area_prefix = 'v'
    kind = 'region'
    svg_map = LAN_MAP


class Kommun(BaseMap):
    """ Swedish Kommun map """
    x_labels = list(KOMMUNER.keys())
    area_names = KOMMUNER
    area_prefix = 'k'
    kind = 'kommun'
    svg_map = KOMMUN_MAP

    def adapt_code(self, area_code):
        """Hook to change the area code"""
        return KOMMUNER.get(area_code, area_code)


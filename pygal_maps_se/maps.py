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
Swiss cantons map

"""

from __future__ import division
from pygal.graph.map import BaseMap
from pygal._compat import u
import os


LAN = {
    'AB': u("AB"),
    'C': u("C"),
    'D': u("D"),
    'E': u("E"),
    'F': u("F"),
    'G': u("G"),
    'H': u("H"),
    'I': u("I"),
    'K': u("K"),
    'M': u("M"),
    'N': u("N"),
    'O': u("O"),
    'S': u("S"),
    'T': u("T"),
    'U': u("U"),
    'X': u("X"),
    'Y': u("Y"),
    'AC': u("AC"),
    'Z': u("Z"),
    'BD': u("BD"),
    'W': u("W"),
}

REGIONER = {
    "Stockholm": u("Stockholm"),
    "Sydost": u("Sydost"),
    "Skane": u("Skane"),
    "Vast": u("Vast"),
    "Mitt": u("Mitt"),
    "Norr": u("Norr"),
}

with open(os.path.join(
        os.path.dirname(__file__),
        'se.lan.svg')) as file:
    LAN_MAP = file.read()


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


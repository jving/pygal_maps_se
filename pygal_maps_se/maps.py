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
from pygal.etree import etree
from pygal.graph.graph import Graph
from pygal.util import alter, cached_property, cut, decorate
import os


LAN = {
    'AB': u("Stockholm"),
    'C': u("Uppsala"),
    'D': u("Södermanland"),
    'E': u("Östergötland"),
    'F': u("Jönköping"),
    'G': u("Kronoberg"),
    'H': u("Kalmar"),
    'I': u("Gotland"),
    'K': u("Blekinge"),
    'M': u("Skåne"),
    'N': u("Halland"),
    'O': u("Västra götaland"),
    'S': u("Värmland"),
    'T': u("Örebro"),
    'U': u("Västmanland"),
    'X': u("Gävleborg"),
    'Y': u("Västernorrland"),
    'AC': u("Västerbotten"),
    'Z': u("Jämtland"),
    'BD': u("Nottbotten"),
    'W': u("Dalarna"),
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


    def _plot(self):
        """Insert a map in the chart and apply data on it"""
        map = etree.fromstring(self.svg_map)
        map.set('width', str(self.view.width))
        map.set('height', str(self.view.height))

        for i, serie in enumerate(self.series):
            safe_vals = list(
                filter(lambda x: x is not None, cut(serie.values, 1))
            )
            if not safe_vals:
                continue
            min_ = min(safe_vals)
            max_ = max(safe_vals)
            for j, (area_code, value) in self.enumerate_values(serie):
                area_code = self.adapt_code(area_code)
                if value is None:
                    continue
                if max_ == min_:
                    ratio = 1
                else:
                    ratio = .3 + .7 * (value - min_) / (max_ - min_)

                areae = map.findall(
                    ".//*[@class='%s%s %s map-element']" %
                    (self.area_prefix, area_code, self.kind)
                )

                if not areae:
                    continue

                for area in areae:
                    cls = area.get('class', '').split(' ')
                    cls.append('color-%d' % i)
                    cls.append('serie-%d' % i)
                    cls.append('series')
                    area.set('class', ' '.join(cls))
                    if getattr(self, 'use_cmap', False):
                        if getattr(self, 'cmap', None) is None:
                            self.cmap = {min_: (16,255,16), max_: (255,16,16)}
                        if value in self.cmap.keys():
                            mcol = self.cmap[value]
                        else:
                            ks = self.cmap.keys()
                            if value < min(ks):
                                mcol = self.cmap[min(ks)]
                            elif value > max(ks):
                                mcol = self.cmap[max(ks)]
                            else:
                                kl = [x for x in ks if x < value][-1]
                                kh = [x for x in ks if x > value][ 0]
                                lc = self.cmap[ kl ]
                                hc = self.cmap[ kh  ]
                                rat = (value-kl)/(kh-kl)
                                mcol = (
                                    int(lc[0]+(hc[0]-lc[0])*rat),
                                    int(lc[1]+(hc[1]-lc[1])*rat),
                                    int(lc[2]+(hc[2]-lc[2])*rat)
                                )

                        mcolor = "#%02x%02x%02x" % mcol
                        area.set('style', 'fill-opacity: %f; fill: %s' % (0.7, mcolor))
                    else:
                        area.set('style', 'fill-opacity: %f' % ratio)
                    metadata = serie.metadata.get(j)

                    if metadata:
                        node = decorate(self.svg, area, metadata)
                        if node != area:
                            area.remove(node)
                            for g in map:
                                if area not in g:
                                    continue
                                index = list(g).index(area)
                                g.remove(area)
                                node.append(area)
                                g.insert(index, node)

                    for node in area:
                        cls = node.get('class', '').split(' ')
                        cls.append('reactive')
                        cls.append('tooltip-trigger')
                        cls.append('map-area')
                        node.set('class', ' '.join(cls))
                        alter(node, metadata)

                    val = self._format(serie, j)
                    self._tooltip_data(area, val, 0, 0, 'auto')

        self.nodes['plot'].append(map)


class VagRegion(BaseMap):
    """ Swedish Vägregion map """
    x_labels = list(REGIONER.keys())
    area_names = REGIONER
    area_prefix = 'v'
    kind = 'region'
    svg_map = LAN_MAP


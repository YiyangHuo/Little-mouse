#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 1/27/20 1:38 AM
#@Author: Yiyang Huo
#@File  : board.py
#board contains virtual map, mouse, the detect map and control the whole game
import os
from src.virtualmap import Virtualmap
from src.map import Map

map_location = os.path.join(os.path.dirname(__file__) + '/../docs/parameter.json')
virtual_map_location = os.path.join(os.path.dirname(__file__) + '/../docs/virtualmap.json')


class Board:
    def __init__(self, virtual):
        #self.mouse = Mouse(virtual, startpoint)
        self.map_ = Map(map_location)

        if virtual:
            self.virtual_map_ = Virtualmap(map_location, virtual_map_location)

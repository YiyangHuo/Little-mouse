#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 1/27/20 1:38 AM
#@Author: Yiyang Huo
#@File  : board.py
#board contains virtual map, mouse, the detect map and control the whole game


map_location = os.path.join(os.path.dirname(__file__) + '/../docs/virtualmap.txt')


class Board:
    def __init__(self, virtual, startpoint):
        self.mouse = Mouse(virtual, startpoint)
        if virtual:
            self.virtual_map = Virtualmap(map_location)
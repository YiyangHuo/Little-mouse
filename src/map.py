#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2/12/20 10:31 PM
#@Author: Yiyang Huo
#@File  : map.py

import json
from src.point import Point

class Map:
    def __init__(self, map_location):
        with open(map_location, "r") as f:
            data = json.load(f)
        self.map_length_ = data["Length_of_map"]
        self.endpoint_ = data["end_point"]
        self.themap_ = []
        for row in range(self.map_length_):
            self.themap_.append([])
            for col in range(self.map_length_):
                n = Point([row, col], self.endpoint_)
                if row == 0:
                    n.walls_[2] = True
                if col == 0:
                    n.walls_[3] = True
                if row == self.map_length_ - 1:
                    n.walls_[0] = True
                if col == self.map_length_ - 1:
                    n.walls_[1] = True
                self.themap_[row].append(n)

    #def print(self):


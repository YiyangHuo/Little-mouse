#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 1/27/20 1:09 AM
# @Author: Yiyang Huo
# @File  : virtualmap.py
# This will create a virtual map when virtual = true

import json

from src.point import Point

look_walls = [[1, 0, 2], [0, 1, 3], [-1, 0, 0], [0, -1, 1]]


class Virtualmap:
    def __init__(self, map_location, virtualmap_location):
        with open(map_location, "r") as f:
            data = json.load(f)
        with open(virtualmap_location, "r") as vir:
            vir_data = json.load(vir)
        self.map_length_ = data["Length_of_map"]
        self.endpoint_ = data["end_point"]
        self.themap_ = []
        self.walls_ = vir_data["walls"]
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
        for wall in self.walls_:
            self.themap_[wall[0]][wall[1]].walls_[wall[2]] = True
            wall[0] += look_walls[wall[2]][0]
            wall[1] += look_walls[wall[2]][1]
            wall[2] = look_walls[wall[2]][2]
            if self.withinRange([wall[0], wall[1]]):
                self.themap_[wall[0]][wall[1]].walls_[wall[2]] = True
        print("* * *\n*   *\n* * *")
        self.print()
    def withinRange(self, point):
        return self.map_length_ > point[0] >= 0 and self.map_length_ > point[1] >= 0

    def haveWall(self, wall_location):
        return self.themap_[wall_location[0]][wall_location[1]].walls_[wall_location[2]]

    def print(self):
        output = ""
        for line in range(2*self.map_length_ + 1):
            output += "*"
            for col in range(self.map_length_):
                row = self.map_length_ - 1 - ((line-1) // 2)
                if line == 0:
                    output += " * *"
                elif line % 2 == 1: #竖行
                    if self.themap_[row][col].walls_[1]:
                        output += "   *"
                    else:
                        output += "    "

                elif line % 2 == 0: #横行
                    if self.themap_[row][col].walls_[2]:
                        output += " * *"
                    else:
                        if self.themap_[row][col].walls_[1]:
                            output += "   *"
                        else:
                            output += "    "

            output += "\n"
        print(output)
    # print(self.walls[0][0]) #jsontest successfully

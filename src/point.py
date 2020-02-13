#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2/12/20 10:10 PM
#@Author: Yiyang Huo
#@File  : point.py
import math

class Point:
    def __init__(self, position, goal):
        self.taxiDist_ = abs(position[0] - goal[0]) + abs(position[1] - goal[1])
        self.discovered_ = False
        self.position_ = position
        self.parent_ = None
        self.walls_ = [False, False, False, False]

    def updateParent(self,p):
        self.parent_ = p

    def getParent(self):
        return self.parent_


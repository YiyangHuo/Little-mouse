#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 1/27/20 1:09 AM
#@Author: Yiyang Huo
#@File  : virtualmap.py
#This will create a virtual map when virtual = true

import json


class Virtualmap:
    def __init__(self, map_location):
        with open(map_location, "r") as f:
            data = json.load(f)
        self.map_length = data["Length_of_map"]
        self.walls = data["walls"]
        self.endpoint = data["end_point"]
        # print(self.walls[0][0]) #jsontest successfully

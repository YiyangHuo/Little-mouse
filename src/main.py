#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 1/27/20 12:53 AM
#@Author: Yiyang Huo
#@File  : main.py
import os
import sys
from src import virtualmap
from src import mouse



def setup(initial_point, virtual):
    if virtual:
        with open(map_location, "r") as f:
            print(f.read())


if __name__ == '__main__':
    print(sys.argv)
    setup([0,0], True)
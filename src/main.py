#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 1/27/20 12:53 AM
#@Author: Yiyang Huo
#@File  : main.py
import os
import sys
from src import virtualmap
from src import mouse
from src.board import Board


if __name__ == '__main__':
    print(sys.argv)
    game_board = Board([0, 0], True)

# geometry.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
# 
# Created by Jongdeog Lee (jlee700@illinois.edu) on 09/12/2018

"""
This file contains geometry functions that relate with Part1 in MP2.
"""

import math
import numpy as np
from const import *


def computeCoordinate(start, length, angle):
    """Compute the end cooridinate based on the given start position, length and angle.
        Args:
            start (tuple): base of the arm link. (x-coordinate, y-coordinate)
            length (int): length of the arm link
            angle (int): degree of the arm link from x-axis to couter-clockwise

        Return:
            End position of the arm link, (x-coordinate, y-coordinate)
    """
    ret = (start[0] + length * math.cos(angle / 180 * math.pi), (start[1] - length * math.sin(angle / 180 * math.pi)))
    return ret

    pass


def doesArmTouchObstacles(armPos, obstacles):
    """Determine whether the given arm links touch obstacles

        Args:
            armPos (list): start and end position of all arm links [(start, end)]
            obstacles (list): x-, y- coordinate and radius of obstacles [(x, y, r)]

        Return:
            True if touched. False it not.
    """
    # if len(obstacles) == 1:
    #     print(obstacles)
    # print(obstacles)
    # x1 = armPos[i][1][0]
    # x2 = armPos[i][0][0]
    # y1 = armPos[i][1][1]
    # y2 = armPos[i][0][1]
    for i in range(len(armPos)):
        # if arm is vertical
        if armPos[i][1][0] - armPos[i][0][0] == 0:
            for ii in range(len(obstacles)):
                if abs(armPos[i][1][0] - obstacles[ii][0]) <= obstacles[ii][2] and max(armPos[i][1][1], armPos[i][0][1]) >= obstacles[ii][1] >= min(armPos[i][1][1], armPos[i][0][1]) \
                        or math.pow(armPos[i][1][0] - obstacles[ii][0], 2) + math.pow(armPos[i][1][1] - obstacles[ii][1], 2) <= math.pow(obstacles[ii][2], 2) \
                        or math.pow(armPos[i][0][0] - obstacles[ii][0], 2) + math.pow(armPos[i][0][1] - obstacles[ii][1], 2) <= math.pow(obstacles[ii][2], 2):
                    # print("vertical", obstacles[ii])
                    return True
        else:
            a = (armPos[i][1][1] - armPos[i][0][1]) / (armPos[i][1][0] - armPos[i][0][0])
            b = armPos[i][0][1] - a * armPos[i][0][0]
            for ii in range(len(obstacles)):
                m = obstacles[ii][0]
                n = obstacles[ii][1]
                r2 = obstacles[ii][2] * obstacles[ii][2]
                crossX = (m + a * n - a * b) / (a * a + 1)
                crossY = (m * a + a * a * n + b) / (a * a + 1)
                delta2 = math.pow(m - crossX, 2) + math.pow(n - crossY, 2)
                if (delta2 <= r2 and (max(armPos[i][1][0], armPos[i][0][0]) >= crossX >= min(armPos[i][1][0], armPos[i][0][0])) and (max(armPos[i][1][1], armPos[i][0][1]) >= crossY >= min(armPos[i][1][1], armPos[i][0][1])))\
                        or math.pow(armPos[i][1][0] - m, 2) + math.pow(armPos[i][1][1] - n, 2) <= r2 \
                        or math.pow(armPos[i][0][0] - m, 2) + math.pow(armPos[i][0][1] - n, 2) <= r2:
                    # if (delta2 <= r2 and (max(armPos[i][1][0], armPos[i][0][0]) >= crossX >= min(armPos[i][1][0], armPos[i][0][0]))):
                    #     if delta2 <= r2:
                    #         print("aaa")
                    #     if (max(armPos[i][1][0], armPos[i][0][0]) >= crossX >= min(armPos[i][1][0], armPos[i][0][0])):
                    #         print("aaaaaaa", crossX, armPos[i][1][0], armPos[i][0][0])
                    # if math.pow(armPos[i][1][0] - m, 2) + math.pow(armPos[i][1][1] - n, 2) <= r2:
                    #     print("bbb")
                    # if math.pow(armPos[i][0][0] - m, 2) + math.pow(armPos[i][0][1] - n, 2) <= r2:
                    #     print("ccc")
                    # print("obstacles", obstacles[ii], i)
                    return True

    return False


def doesArmTouchGoals(armEnd, goals):
    """Determine whether the given arm links touch goals

        Args:
            armEnd (tuple): the arm tick position, (x-coordinate, y-coordinate)
            goals (list): x-, y- coordinate and radius of goals [(x, y, r)]

        Return:
            True if touched. False it not.
    """
    # print(armEnd[0]-goals[0][0], armEnd[1]-goals[0][1], goals[0][2])
    if ((armEnd[0] - goals[0][0]) * (armEnd[0] - goals[0][0]) + (armEnd[1] - goals[0][1]) * (
            armEnd[1] - goals[0][1])) <= goals[0][2] * goals[0][2]:
        return True
    return False


def isArmWithinWindow(armPos, window):
    """Determine whether the given arm stays in the window

        Args:
            armPos (list): start and end position of all arm links [(start, end)]
            window (tuple): (width, height) of the window

        Return:
            True if all parts are in the window. False it not.
    """
    for i in range(len(armPos)):
        x1 = armPos[i][1][0]
        x2 = armPos[i][0][0]
        y1 = armPos[i][1][1]
        y2 = armPos[i][0][1]
        if (x1 < 0) or (x1 > window[0]) or (x2 < 0) or (x2 > window[0]) or (y1 < 0) or (y1 > window[1]) or (y2 < 0) or (y2 > window[1]):
            # print("Border")
            return False
    # print("am i called?")
    return True

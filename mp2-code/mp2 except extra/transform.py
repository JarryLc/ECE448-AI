# transform.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
# 
# Created by Jongdeog Lee (jlee700@illinois.edu) on 09/12/2018

"""
This file contains the transform function that converts the robot arm map
to the maze.
"""
import copy
from arm import Arm
from maze import Maze
from search import *
from geometry import *
from const import *
from util import *





def transformToMaze(arm, goals, obstacles, window, granularity):
    """This function transforms the given 2D map to the maze in MP1.
    
        Args:
            arm (Arm): arm instance
            goals (list): [(x, y, r)] of goals
            obstacles (list): [(x, y, r)] of obstacles
            window (tuple): (width, height) of the window
            granularity (int): unit of increasing/decreasing degree for angles

        Return:
            Maze: the maze instance generated based on input arguments.

    """

    # obstaclesAll = []
    # for i in range(len(obstacles)):
    #     obstaclesAll.append(obstacles[i])
    obstaclesAll = obstacles + goals
    armLimit = arm.getArmLimit()
    rowNum = round(abs(armLimit[0][0] - armLimit[0][1]) / granularity + 1)
    colNum = round(abs(armLimit[1][0] - armLimit[1][1]) / granularity + 1)
    transformMap = []
    # print(rowNum, colNum)
    # print(granularity)
    for i in range(rowNum):
        transformMap.append([])
        for ii in range(colNum):
            transformMap[i].append(" ")

    initArmAngles = arm.getArmAngle()
    print(initArmAngles)

    # arm.setArmAngle([66, -38])
    # print(doesArmTouchObstacles(arm.getArmPos(),obstacles), "test")
    # transformMap[round((armAngles[0] - min(armLimit[0][0], armLimit[0][1])) / (abs(armLimit[0][0] - armLimit[0][1])) * rowNum)]\
    #             [round((armAngles[1] - min(armLimit[1][0], armLimit[1][1])) / (abs(armLimit[1][0] - armLimit[1][1])) * colNum)] = "P"

    # print(round((armAngles[0] - min(armLimit[0][0], armLimit[0][1])) / (abs(armLimit[0][0] - armLimit[0][1])) * rowNum), round((armAngles[1] - min(armLimit[1][0], armLimit[1][1])) / (abs(armLimit[1][0] - armLimit[1][1])) * colNum))
    for i in range(rowNum):
        for ii in range(colNum):
            # print("1")
            angles = [i*granularity + min(armLimit[0][0], armLimit[0][1]), ii*granularity + min(armLimit[1][0], armLimit[1][1])]
            # print(angles)
            arm.setArmAngle(angles)
            if doesArmTouchObstacles(arm.getArmPos(), obstaclesAll) or not isArmWithinWindow(arm.getArmPos(), window):
                # if transformMap[i][ii] == "P":
                #     print("?")
                #     print(arm.getArmPos(), window)
                transformMap[i][ii] = "%"

                # if i == 50 and ii == colNum-1:
                #     print(arm.getArmPos(), obstacles, doesArmTouchObstacles(arm.getArmPos(), obstacles))
            if doesArmTouchGoals(arm.getEnd(), goals) and not (doesArmTouchObstacles(arm.getArmPos(), obstacles) or not isArmWithinWindow(arm.getArmPos(), window)):
                # if transformMap[i][ii] == "P":
                #     print("??")
                #     print(arm.getArmPos(), window)
                if transformMap[i][ii] == "%":
                    print("ops, this point is counted to both obstacles/outside and goals", i, ii)
                transformMap[i][ii] = "."
    transformMap[round((initArmAngles[0] - min(armLimit[0][0], armLimit[0][1])) / granularity)] \
        [round((initArmAngles[1] - min(armLimit[1][0], armLimit[1][1])) / granularity)] = "P"


    # transformMap[1][1] = "P"
    # transformMap[1][2] = "."
    offset = (min(armLimit[0]), min(armLimit[1]))
    retMaze = Maze(transformMap, offset, granularity)


    outputMap = ""
    for beta in range(len(transformMap[0])):
        for alpha in range(len(transformMap)):
            outputMap += transformMap[alpha][beta]
        outputMap += "\n"
    print(outputMap)

    return retMaze

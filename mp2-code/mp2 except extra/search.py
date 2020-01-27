# search.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
# 
# Created by Jongdeog Lee (jlee700@illinois.edu) on 09/12/2018

"""
This file contains search functions.
"""


# Search should return the path and the number of states explored.
# The path should be a list of tuples in the form (alpha, beta, gamma) that correspond
# to the positions of the path taken by your search algorithm.
# Number of states explored should be a number.
# maze is a Maze object based on the maze from the file specified by input filename
# searchMethod is the search method specified by --method flag (bfs,dfs,greedy,astar)
# You may need to slight change your previous search functions in MP1 since this is 3-d maze

def search(maze, searchMethod):
    return {
        "bfs": bfs,
        "dfs": dfs,
        "greedy": greedy,
        "astar": astar,
    }.get(searchMethod, [])(maze)


def bfs(maze):
    # TODO: Write your code here
    class State:
        def __init__(self, position, lastStateIndex):
            self.position = position
            self.lastState = lastStateIndex

    start = State(maze.getStart(), -1)
    # objective = State(maze.getObjectives(), ())

    objective = maze.getObjectives()
    # print(objective)
    queue = [start]
    explored = [maze.getStart()]

    def addState(a):
        queue.append(a)

    def deleteState():
        for index in range(len(queue) - 1):
            queue[index - 1] = queue[index]
        del queue[len(queue) - 1]

    i = 0
    flag = 1
    for iii in range(len(objective)):
        if objective[iii] in explored:
            flag = 0
            break

    while flag:
        if i >= len(queue):
            return [], 0
        neighbors = maze.getNeighbors(queue[i].position[0], queue[i].position[1])
        for indexN in range(len(neighbors)):
            if neighbors[indexN] not in explored:
                queue.append(State(neighbors[indexN], i))
                explored.append(neighbors[indexN])
        i = i + 1
        for iii in range(len(objective)):
            if objective[iii] in explored:
                flag = 0
                break

    # generate the return list
    bfsReturn = []
    i = len(queue) - 1
    while queue[i].position not in objective:
        i = i - 1
    while i != -1:
        bfsReturn.append(queue[i].position)
        i = queue[i].lastState
    bfsReturn.reverse()
    return bfsReturn, 0


def dfs(maze):
    # TODO: Write your code here    
    return [], 0


def greedy(maze):
    # TODO: Write your code here    
    return [], 0


def astar(maze):
    # TODO: Write your code here    
    return [], 0

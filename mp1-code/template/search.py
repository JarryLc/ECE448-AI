# search.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
#
# Created by Michael Abir (abir2@illinois.edu) on 08/28/2018

"""
This is the main entry point for MP1. You should only modify code
within this file -- the unrevised staff files will be used for all other
files and classes when code is run, so be careful to not modify anything else.
"""

import time
# Search should return the path.
# The path should be a list of tuples in the form (row, col) that correspond
# to the positions of the path taken by your search algorithm.
# maze is a Maze object based on the maze from the file specified by input filename
# searchMethod is the search method specified by --method flag (bfs,dfs,astar,astar_multi,extra)


def search(maze, searchMethod):
    return {
        "bfs": bfs,
        "dfs": dfs,
        "astar": astar,
        "astar_multi": astar_multi,
        "extra": extra,
    }.get(searchMethod)(maze)


def bfs(maze):
    """
    Runs BFS for part 1 of the assignment.

    @param maze: The maze to execute the search on.

    @return path: a list of tuples containing the coordinates of each state in the computed path
    """
    # return []
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
    return bfsReturn
    # TODO: Write your code here
    class State:
        def __init__(self, position, lastStateIndex):
            self.position = position
            self.lastState = lastStateIndex

    start = State(maze.getStart(), -1)
    # objective = State(maze.getObjectives(), ())
    objective = maze.getObjectives()

    queue = [start]
    explored = [maze.getStart()]

    def addState(a):
        queue.append(a)

    def deleteState():
        for index in range(len(queue)-1):
            queue[index-1] = queue[index]
        del queue[len(queue)-1]

    i = 0
    while objective[0] not in explored:
        neighbors = maze.getNeighbors(queue[i].position[0], queue[i].position[1])
        for indexN in range(len(neighbors)):
            if neighbors[indexN] not in explored:
                queue.append(State(neighbors[indexN], i))
                explored.append(neighbors[indexN])
        i = i + 1

    # generate the return list
    bfsReturn = []
    i = len(queue)-1
    while queue[i].position != objective[0]:
        i = i - 1
    while i != -1:
        bfsReturn.append(queue[i].position)
        i = queue[i].lastState
    bfsReturn.reverse()
    return bfsReturn


def dfs(maze):
    """
    Runs DFS for part 1 of the assignment.

    @param maze: The maze to execute the search on.

    @return path: a list of tuples containing the coordinates of each state in the computed path
    """
    # TODO: Write your code here
    class State:
        def __init__(self, position, lastStateIndex):
            self.position = position
            self.lastState = lastStateIndex

    start = State(maze.getStart(), -1)
    objective = maze.getObjectives()
    queue = [start]
    explored = [maze.getStart()]

    i = 0
    while objective[0] not in explored:
        flag = 0
        neighbors = maze.getNeighbors(queue[i].position[0], queue[i].position[1])
        # if len(neighbors) > 2:
        #     neighbors[0], neighbors[1] = neighbors[1], neighbors[0]
        #     neighbors[1], neighbors[2] = neighbors[2], neighbors[1]

        for index in range(len(neighbors)):
            if neighbors[index] in explored:
                flag = flag + 1

        if len(neighbors) == flag:
            i = i - 1

        else:
            lasti = i
            i = len(explored) - 1
            for indexN in range(len(neighbors)):
                if neighbors[indexN] not in explored:
                    queue.append(State(neighbors[indexN], lasti))
                    explored.append(neighbors[indexN])
                    i = i + 1
                    break
    # generate the return list
    dfsReturn = []
    i = len(queue)-1
    while queue[i].position != objective[0]:
        i = i - 1
    while i != -1:
        dfsReturn.append(queue[i].position)
        i = queue[i].lastState
    dfsReturn.reverse()
    return dfsReturn



def astar(maze):
    """
    Runs A star for part 1 of the assignment.

    @param maze: The maze to execute the search on.

    @return path: a list of tuples containing the coordinates of each state in the computed path
    """
    # TODO: Write your code here
    class State:
        def __init__(self, position, gs, lastPosition):
            self.position = position
            self.gs = gs
            self.lastPosition = lastPosition

    objective = maze.getObjectives()

    def geths(a):
        return abs(a[0]-objective[0][0])+abs(a[1]-objective[0][1])

    start = State(maze.getStart(), 0, -1)
    priqueue = [start]
    link = [start]
    explored = [maze.getStart()]

    def addPriqueue(f):
        index = 0
        while index in range(len(priqueue)):
            if (priqueue[index].gs + geths(priqueue[index].position)) > (f.gs + geths(f.position)):
                break
            index = index + 1
        priqueue.insert(index, f)

    def indexPriqueue(pos):
        index = 0
        while index in range(len(priqueue)):
            if priqueue[index].position == pos:
                return index
            index = index + 1
        return -1

    def indexLink(pos):
        index = 0
        while index in range(len(link)):
            if link[index].position == pos:
                return index
            index = index + 1
        return -1

    while priqueue[0].position != objective[0]:
        neighbors = maze.getNeighbors(priqueue[0].position[0], priqueue[0].position[1])
        for indexN in range(len(neighbors)):
            if neighbors[indexN] not in explored:
                explored.append(neighbors[indexN])
                frontier = State(neighbors[indexN], priqueue[0].gs + 1, priqueue[0].position)
                addPriqueue(frontier)
                link.append(frontier)
            else:
                updateIndex = indexPriqueue(neighbors[indexN])
                # if the update state is in the priqueue, then update gs directly
                if updateIndex != -1:
                    if priqueue[updateIndex].gs > priqueue[0].gs + 1:
                        frontier = State(neighbors[indexN], priqueue[0].gs + 1, priqueue[0].position)
                        priqueue.pop(updateIndex)
                        addPriqueue(frontier)
                        indexL = indexLink(neighbors[indexN])
                        link.pop(indexL)
                        link.append(frontier)
                else:
                    indexL = indexLink(neighbors[indexN])
                    if link[indexL].gs > priqueue[0].gs + 1:
                        frontier = State(neighbors[indexN], priqueue[0].gs + 1, priqueue[0].position)
                        addPriqueue(frontier)
                        link.pop(indexL)
                        link.append(frontier)
        priqueue.pop(0)

    astarReturn = []
    i = len(link) - 1
    while link[i].position != objective[0]:
        i = i - 1
    while i != -1:
        astarReturn.append(link[i].position)
        i = indexLink(link[i].lastPosition)
    astarReturn.reverse()

    return astarReturn


def astar_multi(maze):
    """
    Runs A star for part 2 of the assignment in the case where there are
    multiple objectives.

    @param maze: The maze to execute the search on.

    @return path: a list of tuples containing the coordinates of each state in the computed path
    """
    # TODO: Write your code here
    class State:
        def __init__(self, position, gs, lastPosition):
            self.position = position
            self.gs = gs
            self.lastPosition = lastPosition

    objective = maze.getObjectives()

    def geths(a, p):
        return abs(a[0] - p[0]) + abs(a[1] - p[1])

    def multiAstar(fromPosition, toPosition):
        start = State(fromPosition, 0, -1)
        priqueue = [start]
        link = [start]
        explored = [fromPosition]

        def addPriqueue(f):
            index = 0
            while index in range(len(priqueue)):
                if (priqueue[index].gs + geths(priqueue[index].position, toPosition)) > \
                        (f.gs + geths(f.position, toPosition)):
                    break
                index = index + 1
            priqueue.insert(index, f)

        def indexPriqueue(pos):
            index = 0
            while index in range(len(priqueue)):
                if priqueue[index].position == pos:
                    return index
                index = index + 1
            return -1

        def indexLink(pos):
            index = 0
            while index in range(len(link)):
                if link[index].position == pos:
                    return index
                index = index + 1
            return -1

        while priqueue[0].position != toPosition:
            neighbors = maze.getNeighbors(priqueue[0].position[0], priqueue[0].position[1])
            for indexN in range(len(neighbors)):
                if neighbors[indexN] not in explored:
                    explored.append(neighbors[indexN])
                    frontier = State(neighbors[indexN], priqueue[0].gs + 1, priqueue[0].position)
                    addPriqueue(frontier)
                    link.append(frontier)
                else:
                    updateIndex = indexPriqueue(neighbors[indexN])
                    # if the update state is in the priqueue, then update gs directly
                    if updateIndex != -1:
                        if priqueue[updateIndex].gs > priqueue[0].gs + 1:
                            frontier = State(neighbors[indexN], priqueue[0].gs + 1, priqueue[0].position)
                            priqueue.pop(updateIndex)
                            addPriqueue(frontier)
                            indexL = indexLink(neighbors[indexN])
                            link.pop(indexL)
                            link.append(frontier)
                    else:
                        indexL = indexLink(neighbors[indexN])
                        if link[indexL].gs > priqueue[0].gs + 1:
                            frontier = State(neighbors[indexN], priqueue[0].gs + 1, priqueue[0].position)
                            addPriqueue(frontier)
                            link.pop(indexL)
                            link.append(frontier)
            priqueue.pop(0)

        astarReturn = []
        i = len(link) - 1
        while link[i].position != toPosition:
            i = i - 1
        while i != -1:
            astarReturn.append(link[i].position)
            i = indexLink(link[i].lastPosition)
        astarReturn.reverse()
        return astarReturn


    objective.insert(0, maze.getStart())
    # print(objective)
    fromList = []
    toList = []
    path = []
    length = []
    indexa = 0
    while indexa in range(len(objective)):
        indexb = indexa + 1
        while indexb < len(objective):
            fromList.append(objective[indexa])
            toList.append(objective[indexb])
            result = multiAstar(objective[indexa], objective[indexb])
            path.append(result)
            length.append(len(result))
            # print(objective[indexa], objective[indexb], len(result))
            indexb = indexb + 1
        indexa = indexa + 1
        # print("+1 astar")

    def mst(a):
        nodeList = []
        for i in range(len(a)):
            if a[i] not in nodeList:
                nodeList.append(a[i])
        # if len(nodeList) > 20:
        #     print("make it easy")
        #     return len(nodeList)

        totalCost = 0
        shortestLength = 500
        shortestIndex = -1
        if len(nodeList) == 1:
            return 0
        for i in range(len(fromList)):
            # print("111", nodeList)
            if (fromList[i] in nodeList) and (toList[i] in nodeList):
                # print("exit")
                    # or ((toList[i] in nodeList) and (fromList[i] in nodeList))
                if length[i] <= shortestLength:
                    shortestLength = length[i]
                    shortestIndex = i
        begining = fromList[shortestIndex]

        # if begining not in nodeList:
            # print(fromList)
            # print(toList)
            # print(nodeList)
            # print(begining)
        u = [begining]
        v = nodeList
        # print("test", v)
        # print(begining)
        v.pop(v.index(begining))
        vFrom = []
        vTo = []
        vLength = []

        while v != []:
            # update vFrom and vLength
            index = 0
            indexL = 0
            # while index in range(len(v)):
            shortestLength = 500
            shortestIndex = -1
            while indexL in range(len(fromList)):
                if ((fromList[indexL] in u) and (toList[indexL] in v)) or \
                        ((toList[indexL] in u) and (fromList[indexL] in v)):
                    # print(length[indexL])
                    if length[indexL] < shortestLength:
                        shortestLength = length[indexL]
                        shortestIndex = indexL
                indexL = indexL + 1
            vFrom.append(fromList[shortestIndex])
            vTo.append(toList[shortestIndex])
            vLength.append(length[shortestIndex])
                # index = index + 1

            # print("1111", vLength)
            # print(vFrom, min(vLength) - 1)
            totalCost = totalCost + min(vLength) - 1
            if vFrom[vLength.index(min(vLength))] in v:
                # print(v)
                pop = v.pop(v.index(vFrom[vLength.index(min(vLength))]))
            else:
                pop = v.pop(v.index(vTo[vLength.index(min(vLength))]))
            u.append(pop)
            # print("u",u)
            # print("v",v)

            vFrom = []
            vTo = []
            vLength = []

        return totalCost





    class Node:
        def __init__(self, position, gs, route, hs):
            self.position = position
            self.gs = gs
            self.route = route
            self.hs = hs

    start = Node(maze.getStart(), 0, [maze.getStart()], 0)
    multiPriqueue = []

    def findLength(f, t):
        index = 0
        while index in range(len(fromList)):
            if (fromList[index] == f and toList[index] == t) or (toList[index] == f and fromList[index] == t):
                return length[index] - 1
            index = index + 1
        return -1

    def findNodeList(list):
        nodeList = []
        for ii in range(len(objective)):
            if objective[ii] not in list:
                nodeList.append(objective[ii])
        nodeList.append(list[len(list)-1])

        # remove redundant
        a = []
        for i in range(len(nodeList)):
            if nodeList[i] not in a:
                a.append(nodeList[i])

        return a

    for index in range(len(objective)):
        if objective[index] != start.position:
            # for i in range(len(multiPriqueue)):
            #     print(multiPriqueue[i].position)
            indexN = 0
            while indexN in range(len(multiPriqueue)):
                # nodeList = findNodeList(indexN)
                # nodeList2 = []
                # for i in range(len(nodeList)):
                #     nodeList2[i] = nodeList[i]
                # nodeList2.pop(nodeList2.index(start.position))
                # if multiPriqueue[indexN].gs + mst(findNodeList(multiPriqueue[indexN].route)) > \
                #     start.gs + mst(findNodeList([start.position, objective[index]])) + findLength(start.position, objective[index]):
                if multiPriqueue[indexN].gs > findLength(start.position, objective[index]):
                    # print(multiPriqueue[indexN].gs, findLength(start.position, objective[index]), objective[index])
                    break
                indexN = indexN + 1
                # print(indexN, multiPriqueue[indexN].gs, mst(findNodeList(multiPriqueue[indexN].route)))
            # print(indexN, "indexN")
            multiPriqueue.insert(indexN, Node(objective[index], start.gs + findLength(start.position, objective[index]), [start.position, objective[index]], 0))
            # for i in range(len(multiPriqueue)):
            #     multiPriqueue[i].hs = mst(findNodeList(multiPriqueue[i].route))
            #     print(multiPriqueue[i].position, multiPriqueue[i].route,
            #           multiPriqueue[i].gs + mst(findNodeList(multiPriqueue[i].route)), multiPriqueue[i].gs,
            #           mst(findNodeList(multiPriqueue[i].route)))
            # print("\n")


    # for i in range(len(multiPriqueue)):
    #     multiPriqueue[i].hs = mst(findNodeList(multiPriqueue[i].route))
    #     print(multiPriqueue[i].position, multiPriqueue[i].route, multiPriqueue[i].gs + mst(findNodeList(multiPriqueue[i].route)), multiPriqueue[i].gs, mst(findNodeList(multiPriqueue[i].route)))

    # while len(multiPriqueue[0].route) < len(objective):
    maxLength = 0
    maxLengthRoute = []

    while 1:
        host = multiPriqueue.pop(0)
        if len(host.route) > maxLength:
            # print(host.route)
            maxLength = len(host.route)
            maxLengthRoute = host.route



        finish = 0
        for i in range(len(objective)):
            if objective[i] not in host.route:
                finish = 0
                break
            else:
                finish = 1
        if finish == 1:
            break

        #     try to improve searching speed
        trashRoute = 0
        for i in range(min(round(maxLength/6), len(host.route))):
            if host.route[i] != maxLengthRoute[i]:
                trashRoute = 1
                break
        if trashRoute == 1:
            # print("delete 1 trash")
            continue

        neighbors = []
        for index in range(len(objective)):
            if objective[index] != host.position and objective[index] not in host.route:
                neighbors.append(objective[index])
        # print("1", host.position)
        for index in range(len(neighbors)):
            flag = 0

            temp = Node(neighbors[index], host.gs + findLength(host.position, neighbors[index]), host.route+[neighbors[index]], 0)
            temp.hs = mst(findNodeList(temp.route))
            # t0 = time.clock()

            if len(multiPriqueue):
                for i in range(len(multiPriqueue)):
                    if multiPriqueue[i].gs + multiPriqueue[i].hs >= temp.gs + temp.hs:
                        break

            multiPriqueue.insert(i, temp)

    finalPath = host.route
    # print(finalPath, len(multiPriqueue), "final")

    finalReturn = []



    for i in range(len(finalPath)-1):
        for ii in range(len(path)):
            if fromList[ii] == finalPath[i] and toList[ii] == finalPath[i+1]:
                finalReturn = finalReturn + path[ii]
                finalReturn.pop()
                break
            elif toList[ii] == finalPath[i] and fromList[ii] == finalPath[i+1]:
                # a = []
                # for iii in range(len(path[ii])):
                #     a.append(path[ii])
                # a.reverse()
                path[ii].reverse()
                finalReturn = finalReturn + path[ii]
                path[ii].reverse()
                finalReturn.pop()
                break


    finalReturn.append(finalPath[len(finalPath)-1])
    # print(finalReturn)




    return finalReturn


def extra(maze):
    # astar_multi(maze)
    """
    Runs extra credit suggestion.

    @param maze: The maze to execute the search on.

    @return path: a list of tuples containing the coordinates of each state in the computed path
    """
    # TODO: Write your code here
    class State:
        def __init__(self, position, gs, lastPosition):
            self.position = position
            self.gs = gs
            self.lastPosition = lastPosition

    objective = maze.getObjectives()

    def geths(a, p):
        return abs(a[0] - p[0]) + abs(a[1] - p[1])

    def multiAstar(fromPosition, toPosition):
        start = State(fromPosition, 0, -1)
        priqueue = [start]
        link = [start]
        explored = [fromPosition]

        def addPriqueue(f):
            index = 0
            while index in range(len(priqueue)):
                if (priqueue[index].gs + geths(priqueue[index].position, toPosition)) > \
                        (f.gs + geths(f.position, toPosition)):
                    break
                index = index + 1
            priqueue.insert(index, f)

        def indexPriqueue(pos):
            index = 0
            while index in range(len(priqueue)):
                if priqueue[index].position == pos:
                    return index
                index = index + 1
            return -1

        def indexLink(pos):
            index = 0
            while index in range(len(link)):
                if link[index].position == pos:
                    return index
                index = index + 1
            return -1

        while priqueue[0].position != toPosition:
            neighbors = maze.getNeighbors(priqueue[0].position[0], priqueue[0].position[1])
            for indexN in range(len(neighbors)):
                if neighbors[indexN] not in explored:
                    explored.append(neighbors[indexN])
                    frontier = State(neighbors[indexN], priqueue[0].gs + 1, priqueue[0].position)
                    addPriqueue(frontier)
                    link.append(frontier)
                else:
                    updateIndex = indexPriqueue(neighbors[indexN])
                    # if the update state is in the priqueue, then update gs directly
                    if updateIndex != -1:
                        if priqueue[updateIndex].gs > priqueue[0].gs + 1:
                            frontier = State(neighbors[indexN], priqueue[0].gs + 1, priqueue[0].position)
                            priqueue.pop(updateIndex)
                            addPriqueue(frontier)
                            indexL = indexLink(neighbors[indexN])
                            link.pop(indexL)
                            link.append(frontier)
                    else:
                        indexL = indexLink(neighbors[indexN])
                        if link[indexL].gs > priqueue[0].gs + 1:
                            frontier = State(neighbors[indexN], priqueue[0].gs + 1, priqueue[0].position)
                            addPriqueue(frontier)
                            link.pop(indexL)
                            link.append(frontier)
            priqueue.pop(0)

        astarReturn = []
        i = len(link) - 1
        while link[i].position != toPosition:
            i = i - 1
        while i != -1:
            astarReturn.append(link[i].position)
            i = indexLink(link[i].lastPosition)
        astarReturn.reverse()
        return astarReturn


    objective.insert(0, maze.getStart())
    # print(objective)
    fromList = []
    toList = []
    path = []
    length = []
    indexa = 0
    while indexa in range(len(objective)):
        indexb = indexa + 1
        while indexb < len(objective):
            fromList.append(objective[indexa])
            toList.append(objective[indexb])
            if (abs(objective[indexa][0] - objective[indexb][0]) == 1 and objective[indexa][1] == objective[indexb][1]) \
                    or (abs(objective[indexa][1] - objective[indexb][1]) == 1 and (objective[indexa][0] == objective[indexb][0])):
                result = [objective[indexa], objective[indexb]]
                # if objective[indexa] == (15, 14) and objective[indexb] == (15, 1):
                #     print("not aaa")
            else:
                result = multiAstar(objective[indexa], objective[indexb])
                # if objective[indexa] == (15, 14) and objective[indexb] == (15, 1):
                #     print("aaaa")
            path.append(result)
            length.append(len(result))
            indexb = indexb + 1
        indexa = indexa + 1
        # print(indexa,"+1 astar")

    def mst(a):
        nodeList = []
        for i in range(len(a)):
            if a[i] not in nodeList:
                nodeList.append(a[i])
        minLength = 500
        indexMin = 0
        for i in range(len(fromList)):
            if nodeList[len(nodeList)-1] == fromList[i] or nodeList[len(nodeList)-1] == toList[i]:
                if minLength > length[i]:
                    minLength = length[i]
                    indexMin = i
        return len(nodeList) - 1 + length[indexMin] - 1




    class Node:
        def __init__(self, position, gs, route, hs):
            self.position = position
            self.gs = gs
            self.route = route
            self.hs = hs

    start = Node(maze.getStart(), 0, [maze.getStart()], 0)
    multiPriqueue = []

    def findLength(f, t):
        index = 0
        while index in range(len(fromList)):
            if (fromList[index] == f and toList[index] == t) or (toList[index] == f and fromList[index] == t):
                return length[index] - 1
            index = index + 1
        return -1

    def findNodeList(list):
        nodeList = []
        for ii in range(len(objective)):
            if objective[ii] not in list:
                nodeList.append(objective[ii])
        nodeList.append(list[len(list)-1])

        # remove redundant
        a = []
        for i in range(len(nodeList)):
            if nodeList[i] not in a:
                a.append(nodeList[i])

        return a

    for index in range(len(objective)):
        if objective[index] != start.position:
            # for i in range(len(multiPriqueue)):
            #     print(multiPriqueue[i].position)
            indexN = 0
            while indexN in range(len(multiPriqueue)):

                if multiPriqueue[indexN].gs > findLength(start.position, objective[index]):

                    break
                indexN = indexN + 1

            multiPriqueue.insert(indexN, Node(objective[index], start.gs + findLength(start.position, objective[index]), [start.position, objective[index]], 0))


    # for i in range(len(multiPriqueue)):
    #     multiPriqueue[i].hs = mst(findNodeList(multiPriqueue[i].route))
    #     print(multiPriqueue[i].position, multiPriqueue[i].route, multiPriqueue[i].gs + mst(findNodeList(multiPriqueue[i].route)), multiPriqueue[i].gs, mst(findNodeList(multiPriqueue[i].route)))

    maxLength = 0
    maxLengthRoute = []
    trashNum = 0

    while 1:
        host = multiPriqueue.pop(0)
        if len(host.route) > maxLength:
            # print(host.route)
            maxLength = len(host.route)
            maxLengthRoute = host.route



        finish = 0
        for i in range(len(objective)):
            if objective[i] not in host.route:
                finish = 0
                break
            else:
                finish = 1
        if finish == 1:
            break

        #     try to improve searching speed
        trashRoute = 0
        # if len(host.route) < 20:
        #     restriction = round(maxLength / 3)
        # elif len(host.route) < 50:
        #     restriction = maxLength - 15
        # elif len(host.route) < 90:
        #     restriction = maxLength - 10
        # elif len(host.route) < 120:
        #     restriction = maxLength - 10
        # elif len(host.route) < 150:
        #     restriction = maxLength - 10
        # elif len(host.route) < 190:
        #     restriction = maxLength - 15
        # else:
        #     restriction = maxLength - 15

        # restriction = round(maxLength / 2)
        restriction = maxLength
        for i in range(min(restriction, len(host.route))):
            if host.route[i] != maxLengthRoute[i]:
                trashRoute = 1
                break
        if trashRoute == 1:
            # print("delete", trashNum, "trash")
            trashNum = trashNum + 1
            continue

        # originalNeighbors = []
        neighbors = []
        minNeighbors = 500
        if len(neighbors) == 0:
            # print("find the nearest")
            for index in range(len(objective)):
                if objective[index] != host.position and objective[index] not in host.route:
                    tempNb = findLength(host.position, objective[index])
                    if minNeighbors > tempNb:
                        minNeighbors = tempNb
                        minIndex = index
            neighbors.append(objective[minIndex])


        for index in range(len(neighbors)):



            temp = Node(neighbors[index], host.gs + findLength(host.position, neighbors[index]), host.route+[neighbors[index]], 0)
            temp.hs = mst(findNodeList(temp.route))
            # t0 = time.clock()

            if len(multiPriqueue):
                for i in range(len(multiPriqueue)):
                    if multiPriqueue[i].gs + multiPriqueue[i].hs >= temp.gs + temp.hs:
                        break

            multiPriqueue.insert(i, temp)

    finalPath = host.route
    # print(finalPath, len(multiPriqueue), "final")

    finalReturn = []



    for i in range(len(finalPath)-1):
        for ii in range(len(path)):
            if fromList[ii] == finalPath[i] and toList[ii] == finalPath[i+1]:
                finalReturn = finalReturn + path[ii]
                finalReturn.pop()
                break
            elif toList[ii] == finalPath[i] and fromList[ii] == finalPath[i+1]:

                path[ii].reverse()
                finalReturn = finalReturn + path[ii]
                path[ii].reverse()
                finalReturn.pop()
                break


    finalReturn.append(finalPath[len(finalPath)-1])
    # print(finalReturn)


    return finalReturn

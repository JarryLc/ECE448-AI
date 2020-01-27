dic = {
    0: [],
    1: [0],
    2: [0],
    3: [1, 2],
    4: [3]
}

flag = 1
available = set()
ret = []
visiting = set()


def dfs(node):
    if node in available:
        return
    visiting.add(node)
    for element in dic[node]:
        if element in visiting:
            raise Exception("11")
        if element not in available:
            dfs(element)
    available.add(node)
    ret.append(node)
    visiting.remove(node)
    # print(ret)
    return


for node in dic:
    dfs(node)

# print(ret)



def pr():
    global flag
    print(flag)
    flag += 1
    print(flag)
pr()
print(flag)

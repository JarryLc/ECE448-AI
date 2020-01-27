插入到sort之后的：


idx = {}
for i,pack in enumerate(packagesSpace):
    if pack in idx.keys():
        idx[pack].append(i)
    else:
        idx[pack] = [i]

packagesSpace = sorted(packagesSpace)
packagesSpace.reverse()
total = truckSpace - 30

for a in packagesSpace:
    left = total - a

    if left in idx.keys():
        if left == a:
            if len(idx) == 1:
                break
            else:
                return [idx[left][0], idx[left][1]]
        else:
            return [idx[left],idx[a]]
return []

if truckSpace <= 30:
    return []

if len(packagesSpace) == 0:
    return []
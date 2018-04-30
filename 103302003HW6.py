GraphList = [[[1, 1, 3.5], [2, 1, 2.8], [3, 2, 1.5]],
             [[1, 0, 3.5], [2, 0, 2.8], [4, 2, 2.9], [5, 3, 5.8]],
             [[3, 0, 1.5], [4, 1, 2.9], [11, 6, 2.3]], 
             [[5, 1, 5.8], [6, 4, 2.4], [7, 5, 3.3]], 
             [[6, 3, 2.4], [8, 5, 1.6], [9, 5, 2.5]], 
             [[7, 3, 3.3], [8, 4, 1.6], [9, 4, 2.5], [10, 6, 1.4]],
             [[10, 5, 1.4], [11, 2, 2.3]]]

def dfs_iterative(adjLists, start, final):
    roadBranch = [3, 4, 3, 3, 3, 4, 2]
    r = [0, 0, 0, 0, 0, 0, 0]
    visited = []
    for i in range(0, 7):
        visited.append(False)
    v = start
    visited[v] = True
    count = 0
    length = 0
    tmpV = 0
    flagFull = False
    roadList = []
    stack = []
    stack.append(start)
    while(count < 3):
        if(count > 0):
            last = stack.pop()
            visited[last] = False
            last = stack.pop()
            r[last] += 1
            stack.append(last)
            roadList.pop()
            v = stack[len(stack)-1]
        while(True):
            if (v == final):
                print('arrive v', v)
                count += 1
                break
            if (r[v] == roadBranch[v]):
                last = stack.pop()
                roadList.pop()
                v = stack[len(stack)-1]
                flagFull = True
            if(count > 1 and not flagFull):
                v = adjLists[v][r[v]][1]
            elif(count > 1):
                last = stack.pop()
                roadList.pop()
                v = stack[len(stack)-1]

            flagFull = False
            print('-----v-----',v)
            tmpV = v
            tmpL = adjLists[tmpV][r[tmpV]][2]
            length += tmpL
            roadList.append(adjLists[tmpV][r[tmpV]][0])
            
            v = adjLists[v][r[tmpV]][1]
            if(not visited[v]):
                visited[v] = True
                stack.append(v)
            else:
                length -= tmpL
                roadList.pop()
                v = tmpV
                r[tmpV] += 1
        print('stack:', stack)
        print('road:', roadList)
        print('length:', "%.1f" %length)
        print()

#start = input('Please input start point:(0~6):')
#final = input('Please input final point:(0~6):')
#s = int(start)
#f = int(final)
dfs_iterative(GraphList, 0, 4)
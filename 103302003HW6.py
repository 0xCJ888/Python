from random import choice
listG = [[[1, 1, 3.5], [2, 1, 2.8], [3, 2, 1.5]],
         [[1, 0, 3.5], [2, 0, 2.8], [4, 2, 2.9], [5, 3, 5.8]],
         [[3, 0, 1.5], [4, 1, 2.9], [11, 6, 2.3]], 
         [[5, 1, 5.8], [6, 4, 2.4], [7, 5, 3.3]], 
         [[6, 3, 2.4], [8, 5, 1.6], [9, 5, 2.5]], 
         [[7, 3, 3.3], [8, 4, 1.6], [9, 4, 2.5], [10, 6, 1.4]],
         [[10, 5, 1.4], [11, 2, 2.3]]]

def dfs_iterative(adjLists, start, final):
    count = 0
    roadList = []
    while(count < 3):
        ActualRoadList = []
        roadName = 0
        length = 0
        stack = []
        stack.append(start)
        visited = []
        for i in range(0, 7):
            visited.append(False)
        isRepeat = False
        while(len(stack)>0):
            v = stack.pop()
            if (v == final):
                break
            if(not visited[v]):
                visited[v] = True
                listnode = []
                for node in adjLists[v]:
                    listnode.append(node)
                flagAdd = True
                while flagAdd:
                    tmp = choice(listnode)
                    if(not visited[tmp[1]]):
                        ActualRoadList.append(tmp[0])
                        length += tmp[2]
                        roadName += tmp[0]
                        
                        stack.append(tmp[1])
                        flagAdd = False
                
        for road in roadList:
            if(road == roadName):
                isRepeat = True
                break
        
        if(not isRepeat):
            roadList.append(roadName)
            count += 1
            print('')
            print('Road :', ActualRoadList)
            print('total length:', "%.1f" %length)

start = input('Please input start point:(0~6):')
final = input('Please input final point:(0~6):')
s = int(start)
f = int(final)
dfs_iterative(listG, s, f)
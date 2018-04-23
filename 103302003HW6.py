from random import choice
listG = [[[1, 1, 3.5], [2, 1, 2.8], [3, 2, 1.5]],
         [[1, 0, 3.5], [2, 0, 2.8], [4, 2, 2.9], [5, 3, 5.8]],
         [[3, 0, 1.5], [4, 1, 2.9], [11, 6, 2.3]], 
         [[5, 1, 5.8], [6, 4, 2.4], [7, 5, 3.3]], 
         [[6, 3, 2.4], [8, 5, 1.6], [9, 5, 2.5]], 
         [[7, 3, 3.3], [8, 4, 1.6], [9, 4, 2.5], [10, 6, 1.4]],
         [[10, 5, 1.4], [11, 2, 2.3]]]

def dfs_iterative(adjLists, start, final):
    stack = []
    stack.append(start)
    n = len(adjLists)
    visited = []
    for i in range(0,n):
        visited.append(False)
         
    while(len(stack)>0):
        v = stack.pop()
        if (v == final):
            break
        if(not visited[v]):
            visited[v] = True
            print('v = ', v, " ")
            stack_aux = []
            listnode = []
            for node in adjLists[v]:
                listnode.append(node[1])
                
            #print('listnode:', listnode)
            flagAdd = True
            while flagAdd:
                tmp = choice(listnode)
                #print('tmp = ', tmp)
                
                if(not visited[tmp]):
                    stack_aux.append(tmp)
                    #print('stack aux: ', stack_aux)
                    stack.append(stack_aux.pop())
                    flagAdd = False
            #while(len(stack_aux)>0):
                #stack.append(stack_aux.pop())
            print(stack)

dfs_iterative(listG, 0, 3)
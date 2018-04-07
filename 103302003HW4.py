# Pascal's triangle

import sys, getopt

# input args
opts, args = getopt.getopt(sys.argv[1:], "no")

#flag -n:True -o:False
flag = True

for op ,value in opts:
    if op == "-n":
        flag = True
    elif op == "-o":
        flag = False
    else:
        print('unknown options')
        exit()

def pascal_triangle(level):
    if level == 0:
        return [1]
    else:
        output = list(range(level+ 1))
        for i in range(0,level+1):
            if i == 0 or i == level:
                output[i] = 1
            else:
                temp = pascal_triangle(level-1)
                output[i] = temp[i] + temp[i-1]
        return output

# test input number
if len(args) == 1:
    if args[0].isdigit():
        level = int(args[0])

else:
    print('Please input level number again')
    exit()
    
if flag: # -n
    for i in range(0,level+1):
        print(pascal_triangle(i))
else: # -o
    print(pascal_triangle(level))
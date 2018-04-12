import random
import math

def randomDir():
    degree = random.uniform(0,360)
    length = random.uniform(0,5)
    return degree, length

def pol2cart(r, theta):
    x = r * math.cos(theta/360*2*math.pi)
    y = r * math.sin(theta/360*2*math.pi)
    return x, y

place = [0., 0.]
count = 0

while math.fabs(place[0]) <= 150. and math.fabs(place[1]) <= 100.:
    deg, leng = randomDir()
    px, py = pol2cart(leng, deg)
    place[0] += px
    place[1] += py
    count += 1
    print("no\tx\ty")
    print(count, "%.5f" %place[0], "%.5f" %place[1])

print()
print('total move count = ', count)
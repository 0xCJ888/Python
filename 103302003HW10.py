import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams.update({'font.size': 25})

fig, ax = plt.subplots()

def plotXzero(number):
    shfit = np.ones(5) * number 
    vx = np.array([0., 0., 1., 1., 0.]) + shfit
    vy = np.array([0, 2, 2, 0, 0])
    ax.plot(vx, vy, color = 'g',linewidth = 3)  

    size = 0.2
    x = np.array([0+size, 0+size, 1-size, 1-size, 0+size]) + shfit
    y = np.array([0+size, 2-size, 2-size, 0+size, 0+size])
    ax.plot(x, y, color = 'g',linewidth = 3)       
    return vx, vy, x, y

def plotXOne(number,times):
    shfit = np.ones(5) * number
    x = (np.array([0., 0.2, 0.2, 0., 0.]) + shfit) * times
    y = np.array([0, 0, 2, 2, 0]) * times
    ax.plot(x, y, color = 'g',linewidth = 3)
    return x, y

def plotXTwo(number):
    shfit = np.ones(13) * number
    x = np.array([0., 0., 0.8, 0.8, 0., 0., 1., 1., 0.2, 0.2, 1., 1., 0.]) + shfit
    y = np.array([0., 1., 1., 1.8, 1.8, 2., 2., 0.8, 0.8, 0.2, 0.2, 0., 0.])
    ax.plot(x, y, color = 'g',linewidth = 3)
    return x, y

def plotXThree(number):
    shfit = np.ones(13) * number
    x = np.array([0., 0., 0.8, 0.8, 0., 0., 0.8, 0.8, 0., 0., 1., 1., 0.]) + shfit
    y = np.array([0., 0.2, 0.2, 0.9, 0.9, 1.1, 1.1, 1.8, 1.8, 2., 2., 0., 0.])
    ax.plot(x, y, color = 'g',linewidth = 3)
    return x, y

def plotCircle():
    t = np.linspace(0, np.pi ,100)
    ax.plot(5 + 4*np.cos(t), 3 + 4*np.sin(t))


plotXOne(0,1)
plotXzero(0.6)
plotXThree(2)
plotXThree(3.4)
plotXzero(4.8)
plotXTwo(6.2)
plotXzero(7.6)
plotXzero(9)
plotXThree(10.4)
plotCircle()
ax.axis('auto')

my_x_ticks = np.arange(0, 13, 2)
plt.xticks(my_x_ticks)
my_y_ticks = np.arange(10)
plt.yticks(my_y_ticks)
plt.show()
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
import random

x = []
y = []
pi = 4
j = 0

plt.style.use('fivethirtyeight')

def animate(i):
    global pi, j
    if j % 2 == 0: pi -= (4/(j*2 + 3))
    else: pi += (4/(j*2 + 3))
    j += 1
    
    x.append(j)
    y.append(pi)
    plt.cla()
    plt.plot(x,y)

animation = FuncAnimation(plt.gcf(), animate, interval = 10)

plt.tight_layout()
plt.show()
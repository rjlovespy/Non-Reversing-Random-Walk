import matplotlib.animation as ani
import matplotlib.pyplot as plt
import numpy as np


def size(n):
    if n>0:
        return 1
    else:
        return -1
    

n, z = 250, []
x = np.zeros(n+1, dtype=int)
y = np.zeros(n+1, dtype=int)
direction = np.array(["East", "West", "North", "South"])


for i in range(n+1):
    step = np.random.choice(direction)
    z.append(step)
    if i == 0:
        continue
    elif i == 1:
        if z[i]=="East":
            x[i]= x[i-1] +1
            y[i]= y[i-1]
        elif z[i]=="West":
            x[i]= x[i-1] -1
            y[i]= y[i-1]   
        elif z[i]=="North":
            x[i]= x[i-1]
            y[i]= y[i-1] +1
        else:
            x[i]= x[i-1]
            y[i]= y[i-1] -1
    else:
        while (((z[i-1] == "East") and (z[i] == "West")) or ((z[i-1] == "West") and (z[i] == "East")) or ((z[i-1] == "North") and (z[i] == "South")) or ((z[i-1] == "South") and (z[i] == "North"))):
            step = np.random.choice(direction)
            z[i] = step
        if z[i] == "East":
            x[i] = x[i-1] + 1
            y[i] = y[i-1]
        elif z[i] == "West":
            x[i] = x[i-1] - 1
            y[i] = y[i-1]
        elif z[i] == "North":
            x[i] = x[i-1]
            y[i] = y[i-1] + 1
        else:
            x[i] = x[i-1]
            y[i] = y[i-1] - 1
    

fig = plt.figure()
canvas = plt.axes(xlim=(min(x)+size(min(x)),max(x)+size(max(x))),ylim= (min(y)+size(min(y)),max(y)+size(max(y))))
drunkard, = canvas.plot(x[0],y[0],marker='*', markerfacecolor="red", markersize =30, label="Drunkard")
step, = canvas.plot(x[0],y[0],marker='.', markerfacecolor="black", markersize =10)
walk, = canvas.plot(x[0],y[0], color="blue")


def journey(i):
    drunkard.set_data(x[i],y[i])         
    step.set_data(x[:i+1],y[:i+1])            
    walk.set_data(x[:i+1],y[:i+1])
    return drunkard, step, walk,


anime=ani.FuncAnimation(fig,journey,frames=n+1,interval= 250,blit=True,repeat=False)     
canvas.plot(x[0],y[0],marker="D",markerfacecolor="gold",markersize=10,label= "Start")
canvas.plot(x[-1],y[-1],marker="D",markerfacecolor="orange",markersize=10,label="End")
canvas.axis(False)
fig.suptitle(f"Non Reversing Random Walk for n = {n} steps")
fig.patch.set_facecolor("lime")
plt.legend(loc="best")
# anime.save("NRRW.gif")
plt.show()

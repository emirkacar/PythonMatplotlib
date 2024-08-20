import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,10,1)
y=np.arange(1,19,2)

fig=plt.figure()
axes = fig.add_axes([0.1,0.2,0.3,0.4])
axes.plot(x,x**2,color="Red",linewidth=2,linestyle="--",marker="o",markersize=15,markerfacecolor="black"
          ,markeredgecolor="yellow",markeredgewidth=4)
axes.set_xlim(0,20)
axes.set_ylim(0,50)
plt.show()
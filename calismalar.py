import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,6)
y = np.arange(2,11,2)


fig,axes=plt.subplots(nrows=2,ncols=1,figsize=(8,6))

axes[0].plot(x,y,color="red")
axes[1].plot(x,y**0.5,color="black")

axes[0].set_title("First axes")
axes[1].set_title("Second axes")


plt.tight_layout()   #Iki grafik uzerinde daha duzgun bir gorunum icin.
plt.show()

fig=plt.figure(figsize=(8,6))
axes = fig.add_axes([0.2,0.3,0.5,0.6])

axes.plot(x,x**0.5,color="red",label="x karekok")
axes.plot(x,x**2,color="yellow",label="x'in karesi")
axes.plot(x,x**3,color="black",label="x'in kupu")

axes.legend()
plt.show()

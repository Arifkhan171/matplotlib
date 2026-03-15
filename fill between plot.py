import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3,4,5])
y=np.array([1,3,5,7,9])
plt.plot(x,y,color="r")
plt.title("phyton")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.fill_between(x,y,color="g",where=(x>=2)&(x<=4))#x=[2,4],y1=2,y2=7,
plt.show()
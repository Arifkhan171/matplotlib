import matplotlib.pyplot as plt
import numpy as np

x=["Arif","ajab","gul","sattar"]
y=[85,60,70,90]
c=["r","b","g","y"]
plt.xlabel("students",fontsize=15)
plt.ylabel("marks",fontsize=15)
plt.title("position",fontsize=20)
plt.bar(x,y,color=c,width=0.3,align="edge",edgecolor="r",linewidth=5,label="mathpaper")#edgecolor="r",  show edges and linewidth=5 show its width
plt.legend() #legend function is for label="mathpaper"
plt.show()




x=["Arif","ajab","gul","sattar"]
y=[69,55,43,24]
z=[80,66,70,66]
width=.5
p=np.arange(len(x))
p1=[j+width for j in p]
plt.xlabel("students",fontsize=15)
plt.ylabel("marks",fontsize=15)
plt.title("position",fontsize=20)
plt.bar(p,y,color="y",width=.5,label="mathpaper",edgecolor="b",linewidth=5)#edgecolor="r",  show edges and linewidth=5 show its width
plt.bar(p1,z,color="r",width=.2,label="englishpaper",edgecolor="b",linewidth=5,linestyle=":",alpha=0.3) # edgecolor="r",  show edges and linewidth=5 show its width
plt.legend() #legend function is for label="mathpaper"

plt.show()
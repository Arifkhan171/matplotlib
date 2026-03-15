import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[1,3,5,7,9]
plt.savefig("line3.jpg",dpi=2000,facecolor="g",transparent=True,bbox_inches="tight")
plt.plot(x,y)
plt.show()
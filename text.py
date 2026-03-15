import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[1,3,5,7,9]
plt.plot(x,y)
plt.title("phyton")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.text(4,5,"python",style="italic",bbox={"facecolor":"red"})
plt.annotate("python",xy=(2,1),xytext=(3,3),arrowprops=dict(facecolor="black",shrink=100))
plt.show()
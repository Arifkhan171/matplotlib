import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[1,3,5,7,9]

plt.grid()
plt.title("phyton")
plt.xlabel("x axis")
plt.ylabel("y axis")



plt.step(x,y,color="r",marker="o",ms=10,mfc='g',label="python")
plt.legend()
plt.show()
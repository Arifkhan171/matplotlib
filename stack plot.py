import matplotlib.pyplot as plt
x=[1,2,3,4,5]
ar1=[1,3,1,7,9]
ar2=[2,4,1,3,5]
ar3=[1,3,1,9,5]
l=["area1","area2","area3"]

plt.stackplot(x,ar1,ar2,ar3,labels=l,colors=["r","g","m"])
plt.title("phyton")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend()
plt.show()
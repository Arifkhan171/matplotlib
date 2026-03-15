import matplotlib.pyplot as plt
x=[10,30,80,50]
y=["c","c++","java","python"]
plt.pie(x,labels=y)
plt.show()


x=[10,30,80,50]
y=["c","c++","java","python"]
e=[0.4,0.0,0.0,0.0]
c=["g","r","y","b"]

plt.pie(x,labels=y,explode=e,colors=c,autopct="%0.2f%%",shadow=True,radius=1.1,labeldistance=1.1,textprops={"fontsize":15},
        wedgeprops={"linewidth":4,"edgecolor":"m"})

plt.title("score")
plt.legend(loc=2)
#plt.pie([1],colors="w") #used for ring chart
plt.show()


import matplotlib.pyplot as plt
from matplotlib.pyplot import colorbar

x=[1,2,3,4,5]
y=[2,5,3,6,9]
plt.scatter(x,y)
plt.show()

day=[1,2,3,4,5]
hour=[2,5,3,6,9]
plt.scatter(day,hour)
plt.title("scatter plot",fontsize=18)
plt.xlabel("days",fontsize=12)
plt.ylabel("hours",fontsize=12)
plt.show()


day=[1,2,3,4,5]
hour=[2,5,3,6,9]
sizes=[200]
colors=[20,22,24,25,26]
# plt.scatter(day,hour,color="r",s= sizes,marker="*",edgecolor="b",linewidths=1)
plt.scatter(day,hour,s= sizes,c=colors,marker="*",cmap="BrBG")
t=plt.colorbar()
t.set_label("colorbar")
plt.title("scatter plot",fontsize=18)
plt.xlabel("days",fontsize=12)
plt.ylabel("hours",fontsize=12)
plt.show()



day=[1,2,3,4,5]
hour=[2,5,3,6,9]
day_2_horse=[3,5,4,2,1]
sizes=[200]
# plt.scatter(day,hour,color="r",s= sizes,marker="*",edgecolor="b",linewidths=1)
plt.scatter(day,hour,s= sizes,color="r",marker="*")
plt.scatter(day,day_2_horse,s= sizes,color="b",marker="*")

plt.title("scatter plot",fontsize=18)
plt.xlabel("days",fontsize=12)
plt.ylabel("hours",fontsize=12)
plt.show()
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[1,3,5,7,9]
plt.subplots()
plt.plot(x,y)

plt.subplots()
plt.pie([1])

x1=[10,20,30,40,50]
plt.subplots()
plt.pie(x1)

x2=["c","c++","java","python"]
y1=[10,20,30,40]
plt.subplots()
plt.bar(x2,y1)

plt.show()
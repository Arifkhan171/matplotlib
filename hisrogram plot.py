import matplotlib.pyplot as plt
import numpy as np
x=np.random.randint(10,60,50)
print(x)

no=[32 ,50 ,10 ,30,59, 44, 30, 55, 58, 53, 54, 31, 53, 47 ,39 ,40 ,29, 52, 47, 27, 59, 54, 47, 59,
 48, 11, 21 ,56, 56, 54, 43, 11, 56, 39, 35, 12, 31, 30, 21, 11, 22, 39, 54, 37 ,49 ,26 ,57 ,39,
 39, 25]
plt.hist(no)
plt.title("histogram plot")
plt.xlabel("python")
plt.ylabel("no")
plt.show()


no=[32 ,50 ,10 ,30,59, 44, 30, 55, 58, 53, 54, 31, 53, 47 ,39 ,40 ,29, 52, 47, 27, 59, 54, 47, 59,
 48, 11, 21 ,56, 56, 54, 43, 11, 56, 39, 35, 12, 31, 30, 21, 11, 22, 39, 54, 37 ,49 ,26 ,57 ,39,
 39, 25]
l=[10,20,30,40,50,60]
plt.hist(no,color="b",bins=l,edgecolor="r",orientation="vertical",rwidth=0.8,label="python no")#  bins till range of data
plt.axvline(45,color="y",label="line")
plt.title("histogram plot")
plt.xlabel("python")
plt.ylabel("no")
plt.legend()
plt.grid()
plt.show()

import matplotlib.pyplot as plt
x=[32 ,50 ,10 ,30,59, 44, 30, 55, 58, 53, 54, 31, 53, 47 ,39 ,40 ,29, 52, 47, 27, 59, 54, 47, 59,
 48, 11, 21 ,56, 56, 54, 43, 11, 56, 39, 35, 12, 31, 30, 21, 11, 22, 39, 54, 37 ,49 ,26 ,57 ,39,
 39, 25,150]
plt.boxplot(x,widths=0.1,label=["python"],patch_artist=True,showmeans=True,sym="r",
            boxprops=dict(color="r"),capprops=dict(color="b"),whiskerprops=dict(color="y")) #whis=3 is used to join line with peak value
plt.show()


x=[32 ,50 ,10 ,30,59, 44, 30]
x2=[58, 53, 54, 31, 53, 47 ,39 ]
y=[x,x2]
plt.boxplot(y,widths=0.1,labels=["python","c"],patch_artist=True,showmeans=True,sym="r",
            boxprops=dict(color="r"),capprops=dict(color="b"),whiskerprops=dict(color="y")) #whis=3 is used to join line with peak value
plt.show()
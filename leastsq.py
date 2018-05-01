#2018.4.28
#第六次作业最小二乘法
#作业：请采用leastsq拟合一条曲线
# y=a*x*x + b*x +c
#
# X:  0,1,2,3,-1,-2,-3
# Y: -1.22,1.85,3.22,10.29,2.21,3.72,8.7
#
# 请尝试写出程序，与课堂上相比，多了一阶。
# 请进一步学习
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.leastsq.html，请理解调用中的func, x0, args三个关键参数。
# 拟合完成的结果需要画图，显示拟合的结果和原来的散点图。
#
# 需要完成时间 < 30分钟。大部分代码用课堂上的代码，然后大家开始修改部分。



import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
plt.figure(figsize= (9,9))
x = np.linspace(-10,10, 1001)
X = np.array([0,1,2,3,-1,-2,-3])
Y = np.array([-1.22,1.85,3.22,10.29,2.21,3.72,8.7])
def f(p):
    a,b,c = p
    return (Y - (a * X * X + b * X + c))
r = leastsq(f, [1, 0,0])

a,b,c = r[0]
print("a = %f b = %f  c = %f" % (a, b ,c))

plt.scatter(X,Y, s=50, alpha=1.0, marker='o',label="data point")

y=a*x*x + b*x + c

ax = plt.gca()

ax.set_xlabel(..., fontsize=20)
ax.set_ylabel(..., fontsize=20)
#设置坐标轴标签字体大小

plt.plot(x, y, color='r',linewidth=3, linestyle=":",markersize=20, label="Curve fitting")

plt.legend(loc=0, numpoints=1)
leg = plt.gca().get_legend()
ltext  = leg.get_texts()
plt.setp(ltext, fontsize='xx-large')

plt.xlabel("X")
plt.ylabel("Y")

plt.xlim(X.min()*1.3, X.max()*1.3)
plt.ylim(Y.min()*1.3, Y.max()*1.3)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
#刻度字体大小
plt.legend(loc='upper left')

plt.show()

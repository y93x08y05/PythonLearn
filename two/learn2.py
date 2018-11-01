# encoding=utf-8
# import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']

names = ['5', '10', '15', '20', '25']
x = range(len(names))
y1 = [0.855, 0.84, 0.835, 0.815, 0.81]
y2 = [0.86, 0.85, 0.853, 0.849, 0.83]

# plt.plot(x, y1, 'ro-')
# plt.plot(x, y2, 'bo-')
# pl.xlim(-1, 11)
# pl.ylim(-1, 110)
plt.plot(x, y1, marker='o', mec='r', mfc='w', label=u'y=x^2曲线图')
plt.plot(x, y2, marker='*', ms=10, label=u'y=x^3曲线图')
plt.legend()
plt.xticks(x, names, rotation=45)
plt.margins(0)
plt.subplots_adjust(bottom=0.15)
plt.xlabel(u"time(s)邻居")
plt.ylabel("RMSE")
plt.show()


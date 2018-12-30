from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']

names = ['100', '200', '300', '400', '500', '600', '700', '800', '900', '1000']
x = range(len(names))
y1 = [222.83, 447.7, 620.25, 848.78, 1064.38, 1288.69, 1544.48, 1700.53, 2013.81, 2285.54]
y2 = [222.7, 445.53, 614.48, 824.4, 1029.48, 1234.83, 1455.44, 1584.71, 1859.82, 2024.07]
plt.plot(x, y1, marker='o', mec='r', mfc='w', label=u'ABC')
plt.plot(x, y2, marker='*', ms=10, label=u'IABC')
plt.legend()
plt.xticks(x, names, rotation=45)
plt.margins(0)
plt.subplots_adjust(bottom=0.15)
plt.xlabel(u"任务数量")
plt.ylabel(u"总完成时间平均值")
plt.title(u"同一虚拟机数量不同任务数量总完成时间平均值对比图")
plt.show()

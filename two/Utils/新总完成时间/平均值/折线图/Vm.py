from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']

names = ['10', '20', '30', '40', '50', '60', '70', '80', '90', '100']
x = range(len(names))
y1 = [6087.04, 2569.32, 1676.67, 1334.4, 1062.8, 1004.21, 798.62, 743.84, 649.54, 595.0]
y2 = [6035.14, 2567.93, 1664.51, 1321.4, 1027.58, 943.68, 741.72, 669.55, 580.57, 520.12]
plt.plot(x, y1, marker='o', mec='r', mfc='w', label=u'ABC')
plt.plot(x, y2, marker='*', ms=10, label=u'IABC')
plt.legend()
plt.xticks(x, names, rotation=45)
plt.margins(0)
plt.ylim(500, 6500)
plt.subplots_adjust(bottom=0.15)
plt.xlabel(u"虚拟机数量")
plt.ylabel(u"总任务完成时间平均值")
plt.title(u"不同虚拟机数量总完成时间平均值对比图")
plt.show()

from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']

names = ['10', '20', '30', '40', '50', '60', '70', '80', '90', '100']
x = range(len(names))
y1 = [51.78, 1.36, 9.31, 8.83, 15.34, 20.57, 14.94, 21.1, 17.81, 15.83]
y2 = [1.26, 1.32, 6.27, 9.19, 6.12, 14.17, 6.6, 13.02, 6.11, 14.43]
plt.plot(x, y1, marker='o', mec='r', mfc='w', label=u'ABC')
plt.plot(x, y2, marker='*', ms=10, label=u'IABC')
plt.legend()
plt.xticks(x, names, rotation=45)
plt.margins(0)
plt.ylim(0, 52)
plt.subplots_adjust(bottom=0.15)
plt.xlabel(u"虚拟机数量")
plt.ylabel(u"总完成时间")
plt.title(u"不同虚拟机数量总完成时间标准差对比图")
plt.show()

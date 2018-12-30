from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']

names = ['10', '20', '30', '40', '50', '60', '70', '80', '90', '100']
x = range(len(names))
y1 = [10.79, 9.4, 15.77, 14.86, 16.9, 21.93, 18.25, 20.57, 21.07, 26.5]
y2 = [9.59, 7.41, 11.67, 12.2, 14.17, 18.41, 15.28, 17.3, 18.2, 25.62]
plt.plot(x, y1, marker='o', mec='r', mfc='w', label=u'ABC')
plt.plot(x, y2, marker='*', ms=10, label=u'IABC')
plt.legend()
plt.xticks(x, names, rotation=45)
plt.margins(0)
plt.ylim(5, 30)
plt.subplots_adjust(bottom=0.15)
plt.xlabel(u"虚拟机数量")
plt.ylabel(u"负载不均衡度")
plt.title(u"不同虚拟机数量负载均衡平均值对比图")
plt.show()

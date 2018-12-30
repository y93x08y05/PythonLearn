from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']

names = ['100', '200', '300', '400', '500', '600', '700', '800', '900', '1000']
x = range(len(names))
y1 = [3.12, 3.75, 5.17, 7.27, 11.5, 21.04, 25.63, 26.43, 38.18, 64.18]
y2 = [3.05, 2.51, 2.99, 4.45, 7.98, 6.46, 10.26, 17.95, 15.22, 8.86]
plt.plot(x, y1, marker='o', mec='r', mfc='w', label=u'ABC')
plt.plot(x, y2, marker='*', ms=10, label=u'IABC')
plt.legend()
plt.xticks(x, names, rotation=45)
plt.margins(0)
plt.subplots_adjust(bottom=0.15)
plt.xlabel(u"任务数量")
plt.ylabel(u"总完成时间标准差")
plt.title(u"不同任务数量总完成时间标准差对比图")
plt.show()

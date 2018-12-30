from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']

names = ['100', '200', '300', '400', '500', '600', '700', '800', '900', '1000']
x = range(len(names))
y1 = [26.01, 23.21, 18.22, 17.42, 17.93, 16.91, 17.18, 15.76, 16.56, 15.91]
y2 = [24.95, 21.45, 15.83, 15.70, 14.23, 13.44, 13.47, 12.44, 12.76, 12.38]
plt.plot(x, y1, marker='o', mec='r', mfc='w', label=u'ABC')
plt.plot(x, y2, marker='*', ms=10, label=u'IABC')
plt.legend()
plt.xticks(x, names, rotation=45)
plt.margins(0)
plt.ylim(10, 30)
plt.subplots_adjust(bottom=0.15)
plt.xlabel(u"任务数量")
plt.ylabel(u"负载不均衡度")
plt.title(u"不同任务数量负载均衡平均值对比图")
plt.show()

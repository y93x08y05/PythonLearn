from pylab import *

mpl.rcParams['font.family'] = 'SimHei'  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号‘-’显示为方块的问题

name_list = ['2014', '2015', '2016', '2017', '2018', '2019', '2020']
IaaS = [150, 180, 220, 300, 400, 500, 560]
PaaS = [10, 20, 30, 40, 50, 60, 70]
SaaS = [260, 316, 450, 520, 600, 720, 820]
plt.bar(range(len(IaaS)), IaaS, label='IaaS', fc='g')
plt.bar(range(len(PaaS)), PaaS, bottom=IaaS, label='PaaS', tick_label=name_list, fc='c')
plt.bar(range(len(SaaS)), SaaS, bottom=IaaS, label='SaaS', tick_label=name_list, fc='m')
plt.legend()
plt.title(u'全球公有云市场规模及其预测（亿美元）')
plt.show()

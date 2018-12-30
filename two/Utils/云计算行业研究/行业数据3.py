from pylab import *

mpl.rcParams['font.family'] = 'SimHei'  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号‘-’显示为方块的问题
# 画堆叠柱状图
data = np.array([[150., 180., 220., 300., 400., 500., 560.],
                 [10., 20., 30., 40., 50., 60., 70.],
                 [260., 316., 450., 520., 600., 720., 820.]])
color_list = ['g', 'c', 'm']
fill_list = ['o', '+', '*']
legend_list = ['IaaS', 'PaaS', 'SaaS']
name_list = ['2014', '2015', '2016', '2017', '2018', '2019', '2020']
X = np.arange(data.shape[1])
for i in range(data.shape[0]):
    plt.bar(X, data[i],
            width=0.5,
            bottom=np.sum(data[:i], axis=0),
            color=color_list[i % len(color_list)],
            label=legend_list[i % len(legend_list)],
            tick_label=name_list,
            alpha=0.5,
            hatch=fill_list[i % len(fill_list)]
            )
plt.legend()
plt.title(u'全球公有云市场规模及其预测（亿美元）')
plt.savefig('全球公有云市场规模及其预测.png')
plt.show()

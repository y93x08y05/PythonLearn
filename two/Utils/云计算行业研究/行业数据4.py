from pylab import *

mpl.rcParams['font.family'] = 'SimHei'  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号‘-’显示为方块的问题
# 画堆叠柱状图
data = np.array([[10.,  30.,  40.,  60.,  100., 200., 300., 400., 600.],
                 [180., 226., 350., 380., 500., 600., 700., 850,  950]])
color_list = ['w', 'm']
fill_list = ['*', 'o']
legend_list = ['公有云规模', '私有云规模']
name_list = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
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
plt.title(u'中国云计算市场规模及其预测（亿美元）')
plt.savefig('中国云计算市场规模及其预测.png')
plt.show()

from pylab import *

mpl.rcParams['font.family'] = 'SimHei'  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号‘-’显示为方块的问题


def plot_data(x1, y1, x3, y3, x4, y4, x6, y6, x7, y7):
    plt.plot(x3, y3, 'c', label=u'ACO')
    plt.plot(x7, y7, 'g', label=u'PSO')
    plt.plot(x4, y4, 'm', label=u'GA')
    plt.plot(x1, y1, 'slateblue', label=u'ABC')
    plt.plot(x6, y6, 'tomato', label=u'IABC')
    plt.legend(fancybox=True)
    plt.margins(0)
    plt.subplots_adjust(bottom=0.15)
    plt.xlabel('迭代次数')
    plt.ylabel('任务总完成时间')
    plt.ylim(250, 550)
    plt.title('基于总完成时间的云计算任务调度')
    # plt.savefig('Vm5Task10Cycle200.png')
    plt.show()


# def plot_data(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7):
#     plt.plot(x1, y1, 'b', label=u'ABC')
#     plt.plot(x2, y2, 'c', label=u'ABCMaxMinMinMin')
#     plt.plot(x3, y3, 'g', label=u'ACO')
#     plt.plot(x4, y4, 'k', label=u'GA')
#     plt.plot(x5, y5, 'm', label=u'IABC')
#     plt.plot(x6, y6, 'r', label=u'IABCMaxMinMinMin')
#     plt.plot(x7, y7, 'y', label=u'PSO')
#     plt.legend(fancybox=True)
#     plt.margins(0)
#     plt.subplots_adjust(bottom=0.15)
#     plt.xlabel('迭代次数')
#     plt.ylabel('任务完成时间')
#     plt.ylim(250, 550)
#     plt.title('基于总完成时间的云计算任务调度')
#     plt.savefig('Vm5Task10Cycle200.png')
#     plt.show()


def load_data(filename):
    in_file = open(filename, 'r')
    x1 = []
    y1 = []
    for line in in_file:
        training_set = line.split(',')
        x1.append(training_set[0])
        y1.append(training_set[1])
        return x1, y1


""" 
plot画图时可以设定线条参数。包括：颜色、线性、标记风格 
（1）控制颜色
    b-blue c-cyan g-green k-black m-magenta r-red w-white y-yellow
    有三种表示颜色的方式
    a.用全名 b.16进制 c.RGB或RGBA元组
（2）控制线型
    符号和线型之间的对应关系
    -  实线
    -- 短线
    -. 短点相间线
    :  虚点线
（3）标记字符
    . 点标记
    ，像素标记
    o 实心圈标记
    v 倒三角标记
    ^ 上三角标记
    > 右三角标记
    < 左三角标记
    * 星型标记
    p 实心五角标记
    s 实心方形标记
    4 右花三角标记
    3 左花三角标记
    2 上花三角标记
    1 下花三角标记
    h 竖六边形标记
    H 横六边形标记
    + 十字标记
    x x标记
    D 菱形标记
    d 瘦菱形标记
    | 垂直线标记
"""

from pylab import *

mpl.rcParams['font.family'] = 'SimHei'  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号‘-’显示为方块的问题


def plot_data(x1, y1, x2, y2, x3, y3, x4, y4, x7, y7):
    plt.plot(x4, y4, 'k', label=u'GA')
    plt.plot(x7, y7, 'y', label=u'PSO')
    plt.plot(x3, y3, 'g', label=u'ACO')
    plt.plot(x1, y1, 'b', label=u'ABC')
    plt.plot(x2, y2, 'c', label=u'IABC')
    plt.legend(fancybox=True)
    plt.margins(0)
    plt.subplots_adjust(bottom=0.15)
    plt.xlabel('迭代次数')
    plt.ylabel('任务完成时间')
    plt.ylim(250, 500)
    plt.title('基于总完成时间的云计算任务调度')
    plt.savefig('Vm10Task30Cycle10000.png')
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
#     # plt.ylim(250, 550)
#     plt.title('基于总完成时间的云计算任务调度')
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
"""

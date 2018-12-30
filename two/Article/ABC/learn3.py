from pylab import *

mpl.rcParams['font.family'] = 'SimHei'  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号‘-’显示为方块的问题


# def plot_data(x1, y1, x2, y2):
#     # plt.plot(x1, y1, x2, y2)
#     plt.plot(x1, y1, 'r', x2, y2, 'b')
#     plt.legend()
#     plt.margins(0)
#     plt.subplots_adjust(bottom=0.15)
#     plt.xlabel('迭代次数')
#     plt.ylabel('任务完成时间')
#     plt.ylim(250, 400)
#     plt.title('基于蜂群算法的云计算任务调度')
#     plt.show()


# def plot_data(x1, y1, x2, y2, x3, y3):
#     plt.plot(x1, y1, 'r', x2, y2, 'b', x3, y3, 'y')
#     plt.legend()
#     plt.margins(0)
#     plt.subplots_adjust(bottom=0.15)
#     plt.xlabel('迭代次数')
#     plt.ylabel('任务完成时间')
#     plt.ylim(250, 500)
#     plt.title('基于蜂群算法的云计算任务调度')
#     plt.show()

def plot_data(x1, y1, x2, y2, x3, y3, x4, y4):
    plt.plot(x1, y1, 'r', label=u'IABC')
    plt.plot(x2, y2, 'b', label=u'ABC')
    plt.plot(x3, y3, 'y', label=u'GA')
    plt.plot(x4, y4, 'g', label=u'PSO')
    plt.legend(fancybox=True)
    plt.margins(0)
    plt.subplots_adjust(bottom=0.15)
    plt.xlabel('迭代次数')
    plt.ylabel('任务完成时间')
    plt.ylim(250, 400)
    plt.title('基于总完成时间的云计算任务调度')
    plt.show()

# def plot_data(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5):
#     plt.plot(x1, y1, 'r', x2, y2, 'b', x3, y3, 'y', x4, y4, 'g', x5, y5, 'm')
#     plt.legend()
#     plt.margins(0)
#     plt.subplots_adjust(bottom=0.15)
#     plt.xlabel('迭代次数')
#     plt.ylabel('任务完成时间')
#     plt.ylim(250, 400)
#     plt.title('基于蜂群算法的云计算任务调度')
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

import numpy as np

from two.Article.虚拟机10个任务30个迭代10000次.画图 import plot_data


# (x1, y1) = np.loadtxt('F:/毕业论文/实验结果/10个虚拟机30个任务10000次迭代/ABC.txt', delimiter=',', unpack=True)
# (x2, y2) = np.loadtxt('F:/毕业论文/实验结果/10个虚拟机30个任务10000次迭代/ABCMaxMinMinMin.txt', delimiter=',', unpack=True)
# (x3, y3) = np.loadtxt('F:/毕业论文/实验结果/10个虚拟机30个任务10000次迭代/ACO.txt', delimiter=',', unpack=True)
# (x4, y4) = np.loadtxt('F:/毕业论文/实验结果/10个虚拟机30个任务10000次迭代/GA.txt', delimiter=',', unpack=True)
# (x5, y5) = np.loadtxt('F:/毕业论文/实验结果/10个虚拟机30个任务10000次迭代/IABC.txt', delimiter=',', unpack=True)
# (x6, y6) = np.loadtxt('F:/毕业论文/实验结果/10个虚拟机30个任务10000次迭代/IABCMaxMinMinMin.txt', delimiter=',', unpack=True)
# (x7, y7) = np.loadtxt('F:/毕业论文/实验结果/10个虚拟机30个任务10000次迭代/PSO.txt', delimiter=',', unpack=True)
# plot_data(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7)

(x1, y1) = np.loadtxt('F:/毕业论文/实验结果/10个虚拟机30个任务10000次迭代/ABC.txt', delimiter=',', unpack=True)
(x2, y2) = np.loadtxt('F:/毕业论文/实验结果/10个虚拟机30个任务10000次迭代/ABCMaxMinMinMin.txt', delimiter=',', unpack=True)
(x3, y3) = np.loadtxt('F:/毕业论文/实验结果/10个虚拟机30个任务10000次迭代/ACO.txt', delimiter=',', unpack=True)
(x4, y4) = np.loadtxt('F:/毕业论文/实验结果/10个虚拟机30个任务10000次迭代/GA.txt', delimiter=',', unpack=True)
# (x5, y5) = np.loadtxt('F:/毕业论文/实验结果/10个虚拟机30个任务10000次迭代/IABC.txt', delimiter=',', unpack=True)
# (x6, y6) = np.loadtxt('F:/毕业论文/实验结果/10个虚拟机30个任务10000次迭代/IABCMaxMinMinMin.txt', delimiter=',', unpack=True)
(x7, y7) = np.loadtxt('F:/毕业论文/实验结果/10个虚拟机30个任务10000次迭代/PSO.txt', delimiter=',', unpack=True)
plot_data(x1, y1, x2, y2, x3, y3, x4, y4, x7, y7)



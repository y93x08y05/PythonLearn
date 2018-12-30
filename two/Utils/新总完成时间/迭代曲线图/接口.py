import numpy as np

from two.Utils.新总完成时间.迭代曲线图.画图 import plot_data


(x1, y1) = np.loadtxt('F:/毕业论文/实验结果/多组结果/虚拟机变/V100/迭代曲线图/ABC-10.txt', delimiter=',', unpack=True)
(x2, y2) = np.loadtxt('F:/毕业论文/实验结果/多组结果/虚拟机变/V100/迭代曲线图/HD-18.txt', delimiter=',', unpack=True)
plot_data(x1, y1, x2, y2)



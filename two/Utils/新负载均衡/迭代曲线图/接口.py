import numpy as np

from two.Utils.新负载均衡.迭代曲线图.画图 import plot_data


(x1, y1) = np.loadtxt('F:/毕业论文/实验结果/新负载均衡/任务变/T600/迭代曲线图/ABC-17.txt', delimiter=',', unpack=True)
(x2, y2) = np.loadtxt('F:/毕业论文/实验结果/新负载均衡/任务变/T600/迭代曲线图/HD-24.txt', delimiter=',', unpack=True)
plot_data(x1, y1, x2, y2)



import numpy as np

from two.Utils.遗传算法.画图 import plot_data

(x, y) = np.loadtxt('F:/毕业论文/实验结果/2018-10-22-14-13-8-GA.txt', delimiter=',', unpack=True)
plot_data(x, y)

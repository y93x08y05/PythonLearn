import numpy as np

from two.Utils.平均完成时间.虚拟机10.画图 import plot_data

(x1, y1) = np.loadtxt('F:/毕业论文/实验结果/平均完成时间/虚拟机10/ABC120.txt', delimiter=',', unpack=True)
(x2, y2) = np.loadtxt('F:/毕业论文/实验结果/平均完成时间/虚拟机10/ABC40.txt', delimiter=',', unpack=True)
(x3, y3) = np.loadtxt('F:/毕业论文/实验结果/平均完成时间/虚拟机10/ABC60.txt', delimiter=',', unpack=True)
(x4, y4) = np.loadtxt('F:/毕业论文/实验结果/平均完成时间/虚拟机10/ABC80.txt', delimiter=',', unpack=True)
(x5, y5) = np.loadtxt('F:/毕业论文/实验结果/平均完成时间/虚拟机10/ABC100.txt', delimiter=',', unpack=True)

# (x1, y1) = np.loadtxt('F:/毕业论文/实验结果/平均完成时间/虚拟机10/GA.txt', delimiter=',', unpack=True)
# (x2, y2) = np.loadtxt('F:/毕业论文/实验结果/平均完成时间/虚拟机10/PSO.txt', delimiter=',', unpack=True)
# (x3, y3) = np.loadtxt('F:/毕业论文/实验结果/平均完成时间/虚拟机10/ACO.txt', delimiter=',', unpack=True)
# (x4, y4) = np.loadtxt('F:/毕业论文/实验结果/平均完成时间/虚拟机10/ABC.txt', delimiter=',', unpack=True)
# (x5, y5) = np.loadtxt('F:/毕业论文/实验结果/平均完成时间/虚拟机10/IABC.txt', delimiter=',', unpack=True)
plot_data(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5)



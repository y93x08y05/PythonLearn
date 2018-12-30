import numpy as np

from two.Utils.负载均衡.虚拟机5.画图 import plot_data

(x1, y1) = np.loadtxt('F:/毕业论文/实验结果/负载均衡/虚拟机5/ABC.txt', delimiter=',', unpack=True)
(x2, y2) = np.loadtxt('F:/毕业论文/实验结果/负载均衡/虚拟机5/ACO.txt', delimiter=',', unpack=True)
(x3, y3) = np.loadtxt('F:/毕业论文/实验结果/负载均衡/虚拟机5/GA.txt', delimiter=',', unpack=True)
(x4, y4) = np.loadtxt('F:/毕业论文/实验结果/负载均衡/虚拟机5/SCA.txt', delimiter=',', unpack=True)
(x5, y5) = np.loadtxt('F:/毕业论文/实验结果/负载均衡/虚拟机5/PSO.txt', delimiter=',', unpack=True)
(x6, y6) = np.loadtxt('F:/毕业论文/实验结果/负载均衡/虚拟机5/IABC.txt', delimiter=',', unpack=True)
plot_data(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6)



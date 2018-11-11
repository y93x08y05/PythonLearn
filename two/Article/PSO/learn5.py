import numpy as np

from two.Article.PSO.learn3 import plot_data

(x, y) = np.loadtxt('F:/毕业论文/实验结果/粒子群算法结果图.txt', delimiter=',', unpack=True)
plot_data(x, y)

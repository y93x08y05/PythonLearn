import numpy as np

from two.Article.GA.learn3 import plot_data

(x, y) = np.loadtxt('F:/毕业论文/实验结果/遗传算法结果图.txt', delimiter=',', unpack=True)
plot_data(x, y)

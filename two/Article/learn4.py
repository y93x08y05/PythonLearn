import numpy as np

from two.Article.learn3 import plot_data

(x, y) = np.loadtxt('F:/毕业论文/实验结果/蚁群算法结果图.txt', delimiter=',', unpack=True)
plot_data(x, y)



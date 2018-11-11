import numpy as np

from two.Article.ABC.learn3 import plot_data

(x, y) = np.loadtxt('F:/毕业论文/实验结果/蜂群算法结果图.txt', delimiter=',', unpack=True)
plot_data(x, y)



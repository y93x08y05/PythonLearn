# coding:utf-8
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'NSimSun,Times New Roman'

x, y = np.loadtxt('F:/毕业论文/实验结果/粒子群算法结果图.txt', delimiter=',', unpack=True)
plt.plot(x, y, label='难度值为30', color='black')
plt.plot(x, y, 'o', color='red')

plt.xlabel(u'迭代次数')
plt.ylabel(u'B')
plt.title('C')
plt.legend()
plt.show()

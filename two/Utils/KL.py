from sympy import *
from pandas import DataFrame
import matplotlib.pyplot as plt
import random
import numpy as np

base = 100
pwin = 0.6
ploss = 1 - pwin
b = 1
c = 1
rnd_position = 0.25
rnd_position2 = 0.15
kelly_position = (pwin * b - ploss) / b
stopline = 1
print('kelly position is %s' % kelly_position)
port_A = DataFrame()
port_B = DataFrame()
port_C = DataFrame()
port_D = DataFrame()
# 重复模拟次数
for i in range(1000):
    port1 = [base]
    port2 = [base]
    port3 = [base]
    port4 = [base]
    # 游戏进行次数
    for step in range(200):
        rnd = random.random()
        if rnd < pwin:
            next_step = b
        else:
            next_step = -c
        if port1[-1] > base * (1 - stopline):
            port1.append(port1[-1] * (1 + next_step))
        else:
            port1.append(port1[-1])
        if port2[-1] > base * (1 - stopline):
            port2.append(port2[-1] * (1 + next_step * kelly_position))
        else:
            port2.append(port2[-1])
        if port3[-1] > base * (1 - stopline):
            port3.append(port3[-1] * (1 + next_step * rnd_position))
        else:
            port3.append(port3[-1])
        if port4[-1] > base * (1 - stopline):
            port4.append(port4[-1] * (1 + next_step * rnd_position2))
        else:
            port4.append(port4[-1])
    port_A[i] = port1
    port_B[i] = port2
    port_C[i] = port3
    port_D[i] = port4


def cal(x):
    if x is not 0:
        y = np.exp(np.sum(np.log(x)) / 1000)
    else:
        y = 0
    return y


plt.figure(figsize=(8, 5))
plt.plot(np.exp(np.log(port_A.T).sum() / 1000), label='port1:full')
plt.plot(np.exp(np.log(port_B.T).sum() / 1000), '*', label='port2:kelly')
plt.plot(np.exp(np.log(port_C.T).sum() / 1000), label='port3:0.25')
plt.plot(np.exp(np.log(port_D.T).sum() / 1000), label='port4:0.15')
plt.legend(loc=0)
plt.show()
print('\n不同组合的几何期望收益')
print('full position %s' % np.exp(np.log(port_A.T).sum() / 1000).iloc[-1])
print('kelly position %s' % np.exp(np.log(port_B.T).sum() / 1000).iloc[-1])
print('position = 0.25 %s' % np.exp(np.log(port_C.T).sum() / 1000).iloc[-1])
print('position = 0.15 %s' % np.exp(np.log(port_D.T).sum() / 1000).iloc[-1])


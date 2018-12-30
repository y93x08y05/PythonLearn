import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib.font_manager import FontManager

custom_font = mpl.font_manager.FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)
font_size = 8
fig_size = (8, 6)
names = (u'ABC', u'IABC')
subjects = ('10', '20', '30', '40', '50', '60', '70', '80', '90', '100')
scores = ((6087.04, 2569.32, 1676.67, 1334.4, 1062.8, 1004.21, 798.62, 743.84, 649.54, 595.0),
          (6035.14, 2567.93, 1664.51, 1321.4, 1027.58, 943.68, 741.72, 669.55, 580.57, 520.12))
mpl.rcParams['font.size'] = font_size
mpl.rcParams['figure.figsize'] = fig_size
bar_width = 0.40
index = np.arange(len(scores[0]))
rects1 = plt.bar(index, scores[0], bar_width, color='#0072BC', label=names[0])
rects2 = plt.bar(index + bar_width, scores[1], bar_width, color='#ED1C24', label=names[1])
plt.xticks(index + bar_width, subjects, fontProperties=custom_font)
plt.ylim(ymax=6500, ymin=0)
plt.xlabel(u'虚拟机数量', fontProperties=custom_font)
plt.ylabel(u'总完成时间', fontProperties=custom_font)
plt.title(u"不同虚拟机数量总完成时间平均值对比图", fontProperties=custom_font)
plt.legend(fancybox=True, prop=custom_font)
plt.show()

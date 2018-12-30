import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib.font_manager import FontManager

custom_font = mpl.font_manager.FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)
font_size = 10
fig_size = (8, 6)
names = (u'粒子群算法', u'人工蜂群算法')
subjects = (u'100', u'200', u'300')
scores = ((26.2, 52.4, 79.4), (20.5, 46.8, 61.5))
mpl.rcParams['font.size'] = font_size
mpl.rcParams['figure.figsize'] = fig_size
bar_width = 0.30
index = np.arange(len(scores[0]))
rects1 = plt.bar(index, scores[0], bar_width, color='#0072BC', label=names[0])
rects2 = plt.bar(index + bar_width, scores[1], bar_width, color='#ED1C24', label=names[1])
plt.xticks(index + bar_width, subjects, fontProperties=custom_font)
plt.ylim(ymax=100, ymin=0)
plt.xlabel(u'任务数量', fontProperties=custom_font)
plt.ylabel(u'任务执行时间', fontProperties=custom_font)
plt.title(u'任务调度', fontProperties=custom_font)
plt.legend(fancybox=True, prop=custom_font)


def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, height, ha='center', va='bottom')
        rect.set_edgecolor('white')


add_labels(rects1)
add_labels(rects2)

plt.savefig('scores_par.png')
plt.show()

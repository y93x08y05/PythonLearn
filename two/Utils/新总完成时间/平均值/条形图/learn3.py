import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib.font_manager import FontManager

custom_font = mpl.font_manager.FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)
font_size = 8
fig_size = (8, 6)
names = (u'ABC', u'IABC')
subjects = ('100', '200', '300', '400', '500', '600', '700', '800', '900', '1000')
scores = ((222.83, 447.7, 620.25, 848.78, 1064.38, 1288.69, 1544.48, 1700.53, 2013.81, 2285.54),
          (222.7, 445.53, 614.48, 824.4, 1029.48, 1234.83, 1455.44, 1584.71, 1859.82, 2024.07))
mpl.rcParams['font.size'] = font_size
mpl.rcParams['figure.figsize'] = fig_size
bar_width = 0.40
index = np.arange(len(scores[0]))
rects1 = plt.bar(index, scores[0], bar_width, color='#0072BC', label=names[0])
rects2 = plt.bar(index + bar_width, scores[1], bar_width, color='#ED1C24', label=names[1])
plt.xticks(index + bar_width, subjects, fontProperties=custom_font)
plt.ylim(ymax=2500, ymin=0)
plt.xlabel(u'任务数量', fontProperties=custom_font)
plt.ylabel(u'总完成时间平均值', fontProperties=custom_font)
plt.title(u"不同任务数量总完成时间平均值对比图", fontProperties=custom_font)
plt.legend(fancybox=True, prop=custom_font)
plt.show()

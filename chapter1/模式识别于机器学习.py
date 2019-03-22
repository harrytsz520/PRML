#!/usr/bin/env python
# coding: utf-8

# 模式识别于机器学习

# 1.绪论

# In[98]:


import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

x = np.linspace(0, 1, 10) 
y = np.sin(2*np.pi*x) + 0.8*np.random.normal()
x1 = np.linspace(0, 1, 100)
y1 = np.sin(2*np.pi*x1)

plt.figure(figsize=(16, 16), dpi=70, facecolor='green', edgecolor='white', frameon=True)
plt.subplot(221)
line1 = plt.scatter(x, y, c='red', marker='*')
line2, = plt.plot(x1, y1, c='green', )
plt.xlim(-0.2, 1.2)
plt.ylim(-1.2, 1.2)
plt.title("多项式曲线拟合")
plt.legend(handles = [line1, line2], labels = ['样本值', '正弦曲线'], loc='best')

plt.show()


# In[ ]:





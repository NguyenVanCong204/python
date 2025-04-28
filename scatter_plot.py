import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([1, 3, 2, 7, 8, 8, 9, 10, 12, 9])
n = np.size(x)

# Tạo màu ngẫu nhiên cho các điểm
colors = np.random.rand(n)
area = 50

# Vẽ scatter plot
plt.scatter(x, y, area, colors, alpha=0.5)
plt.show()
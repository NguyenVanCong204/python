import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Tạo 10 điểm dữ liệu ngẫu nhiên
np.random.seed(42)  # Đặt seed để kết quả có thể tái tạo
x = np.random.rand(10, 1)  # Tạo 10 giá trị ngẫu nhiên cho trục x (dạng 2D array cho sklearn)
y = 2 * x + 0.5 + np.random.randn(10, 1) * 0.1  # Tạo y tuyến tính với x, thêm nhiễu nhỏ

# Tạo và huấn luyện mô hình hồi quy tuyến tính
model = LinearRegression()
model.fit(x, y)

# Lấy w0 (intercept) và w1 (slope)
w0 = model.intercept_[0]  # Điểm chặn
w1 = model.coef_[0][0]    # Hệ số đường thẳng

# Tính R-squared
r_squared = model.score(x, y)

# In kết quả
print(f"Điểm chặn (w0): {w0:.4f}")
print(f"Hệ số đường thẳng (w1): {w1:.4f}")
print(f"R-squared: {r_squared:.4f}")

# Vẽ biểu đồ
# Vẽ scatter plot của dữ liệu
plt.scatter(x, y, color='blue', alpha=0.6, label='Dữ liệu')

# Vẽ đường hồi quy
y_pred = model.predict(x)
plt.plot(x, y_pred, color='red', label='Đường hồi quy')

# Thêm nhãn và tiêu đề
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Hồi quy tuyến tính với 10 điểm ngẫu nhiên')
plt.legend()
plt.grid(True)

# Hiển thị biểu đồ
plt.show()
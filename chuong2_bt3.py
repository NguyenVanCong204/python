import numpy as np

# Tạo 10 điểm dữ liệu ngẫu nhiên (giống như trước để nhất quán)
np.random.seed(42)  # Đặt seed để kết quả có thể tái tạo
x = np.random.rand(10)  # Tạo 10 giá trị ngẫu nhiên cho trục x
y = 2 * x + 0.5 + np.random.randn(10) * 0.1  # Tạo y tuyến tính với x, thêm nhiễu nhỏ

# Tính các tổng cần thiết theo công thức
n = len(x)  # Số lượng điểm dữ liệu

# Tính tổng x, y, x*y, và x^2
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x**2)

# Tính w1
numerator_w1 = sum_xy - (1/n) * sum_x * sum_y  # Tử số
denominator_w1 = sum_x2 - (1/n) * (sum_x)**2   # Mẫu số
w1 = numerator_w1 / denominator_w1

# Tính w0
w0 = (sum_y / n) - w1 * (sum_x / n)

# In kết quả
print(f"Điểm chặn (w0): {w0:.4f}")
print(f"Hệ số đường thẳng (w1): {w1:.4f}")
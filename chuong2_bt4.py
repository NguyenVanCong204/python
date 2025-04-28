import numpy as np
import matplotlib.pyplot as plt

# Tạo 10 điểm dữ liệu ngẫu nhiên (giống như trước để nhất quán)
np.random.seed(42)  # Đặt seed để kết quả có thể tái tạo
x = np.random.rand(10)  # Tạo 10 giá trị ngẫu nhiên cho trục x
y = 2 * x + 0.5 + np.random.randn(10) * 0.1  # Tạo y tuyến tính với x, thêm nhiễu nhỏ

# Tính w0 và w1 theo công thức Least-Squares từ slide
n = len(x)  # Số lượng điểm dữ liệu

# Tính các tổng cần thiết
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

# Vẽ biểu đồ
# Vẽ scatter plot của dữ liệu
plt.scatter(x, y, color='blue', alpha=0.6, label='Dữ liệu')

# Tạo đường thẳng hồi quy dựa trên w0 và w1
# Tạo mảng x mới để vẽ đường thẳng (từ min(x) đến max(x))
x_line = np.linspace(min(x), max(x), 100)  # Tạo 100 điểm từ min(x) đến max(x)
y_line = w0 + w1 * x_line  # Công thức đường thẳng: y = w0 + w1*x

# Vẽ đường thẳng
plt.plot(x_line, y_line, color='red', label='Đường hồi quy')

# Thêm nhãn và tiêu đề
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Đường hồi quy tuyến tính với 10 điểm ngẫu nhiên')
plt.legend()
plt.grid(True)

# Hiển thị biểu đồ
plt.show()

# In w0 và w1 để kiểm tra
print(f"Điểm chặn (w0): {w0:.4f}")
print(f"Hệ số đường thẳng (w1): {w1:.4f}")
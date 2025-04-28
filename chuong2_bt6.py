import numpy as np
import matplotlib.pyplot as plt

# Tạo 10 điểm dữ liệu ngẫu nhiên ban đầu (giống như trước để nhất quán)
np.random.seed(42)  # Đặt seed để kết quả có thể tái tạo
x_initial = np.random.rand(10)  # Tạo 10 giá trị ngẫu nhiên cho trục x
y_initial = 2 * x_initial + 0.5 + np.random.randn(10) * 0.1  # Tạo y tuyến tính với x, thêm nhiễu nhỏ

# Tạo thêm 1 điểm dữ liệu cách xa (outlier)
# Chọn một giá trị x rất lớn (ví dụ: 10) và y tương ứng (giả sử theo xu hướng tuyến tính ban đầu)
x_new = np.array([10])  # Thêm điểm x cách xa (10, ngoài khoảng [0, 1])
y_new = 2 * x_new + 0.5 + np.random.randn(1) * 0.1  # Tính y tương ứng, thêm nhiễu nhỏ

# Kết hợp dữ liệu mới với dữ liệu ban đầu
x = np.concatenate((x_initial, x_new))  # Gộp x ban đầu và x mới
y = np.concatenate((y_initial, y_new))  # Gộp y ban đầu và y mới

# Tính w0 và w1 theo công thức Least-Squares từ slide
n = len(x)  # Số lượng điểm dữ liệu (bây giờ là 11)

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
# Vẽ scatter plot của dữ liệu (10 điểm ban đầu màu xanh, 1 điểm ngoại lai màu đỏ)
plt.scatter(x_initial, y_initial, color='blue', alpha=0.6, label='10 điểm ban đầu')
plt.scatter(x_new, y_new, color='red', s=100, label='Điểm ngoại lai')  # Điểm ngoại lai lớn hơn để dễ nhận diện

# Tạo đường thẳng hồi quy dựa trên w0 và w1
# Tạo mảng x mới để vẽ đường thẳng (từ min(x) đến max(x))
x_line = np.linspace(min(x), max(x), 100)  # Tạo 100 điểm từ min(x) đến max(x)
y_line = w0 + w1 * x_line  # Công thức đường thẳng: y = w0 + w1*x

# Vẽ đường thẳng
plt.plot(x_line, y_line, color='green', label='Đường hồi quy')

# Thêm nhãn và tiêu đề
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Đường hồi quy tuyến tính với 11 điểm (bao gồm điểm ngoại lai)')
plt.legend()
plt.grid(True)

# Hiển thị biểu đồ
plt.show()

# In w0 và w1 để kiểm tra
print(f"Điểm chặn (w0): {w0:.4f}")
print(f"Hệ số đường thẳng (w1): {w1:.4f}")
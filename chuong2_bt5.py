import numpy as np

# Tạo 10 điểm dữ liệu ngẫu nhiên (giống như trước để nhất quán)
np.random.seed(42)  # Đặt seed để kết quả có thể tái tạo
x = np.random.rand(10)  # Tạo 10 giá trị ngẫu nhiên cho trục x
y = 2 * x + 0.5 + np.random.randn(10) * 0.1  # Tạo y tuyến tính với x, thêm nhiễu nhỏ

# Tính w0 và w1 theo công thức Least-Squares từ slide (như trong câu hỏi trước)
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

# Tính giá trị dự đoán y_pred dựa trên w0 và w1
y_pred = w0 + w1 * x

# Tính RSS (Residual Sum of Squares)
e = y - y_pred  # Sai số (lệch giữa giá trị thực tế và dự đoán)
RSS = np.sum(e**2)

# Tính TSS (Total Sum of Squares)
y_mean = np.mean(y)  # Trung bình giá trị y
TSS = np.sum((y - y_mean)**2)

# Tính R-squared
R_squared = 1 - (RSS / TSS)

# In kết quả
print(f"R-squared: {R_squared:.4f}")
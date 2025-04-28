import numpy as np
import matplotlib.pyplot as plt

    def create_random_scatter(n_points=10, x_range=(0,1), y_range=(0,1)):
        # Tạo dữ liệu ngẫu nhiên với phạm vi tùy chỉnh
        x = np.random.uniform(x_range[0], x_range[1], n_points)
        y = np.random.uniform(y_range[0], y_range[1], n_points)
        
        # Tạo figure với kích thước tùy chỉnh
        plt.figure(figsize=(8, 6))
        
        # Vẽ scatter plot với nhiều tùy chỉnh hơn
        plt.scatter(x, y, color='blue', alpha=0.6, s=100, marker='o')
        
        # Thêm nhãn và tiêu đề với font size rõ ràng
        plt.xlabel('X', fontsize=12)
        plt.ylabel('Y', fontsize=12)
        plt.title('Biểu Đồ Phân Tán Điểm Dữ Liệu Ngẫu Nhiên', fontsize=14)
        
        # Tùy chỉnh lưới
        plt.grid(True, linestyle='--', alpha=0.7)
        
        # Thêm giới hạn trục
        plt.xlim(x_range)
        plt.ylim(y_range)
        
        plt.tight_layout()
        plt.show()

    # Gọi hàm với tham số mặc định
    create_random_scatter()
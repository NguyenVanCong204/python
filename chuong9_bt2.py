class Student:
    # Biến class variable dùng chung cho tất cả sinh viên
    school_name = "ABC High School"
    student_list = []

    def __init__(self, student_id, name):
        # Biến instance variable cho từng sinh viên cụ thể
        self.student_id = student_id
        self.name = name
        
        # Khi tạo một đối tượng mới, thêm nó vào danh sách student_list
        Student.student_list.append(self)

# Tạo hai sinh viên
student1 = Student(1, "Cong")
student2 = Student(2, "Minh")

# In thông tin của các đối tượng
# print("student1")
# print("Id : ",student1.student_id)
# print("Name : ",student1.name)
# print("School : ",Student.school_name)
# print("----------------------")
# print("student2")
# print("Id : ",student2.student_id)
# print("Name : ",student2.name)
# print("School : ",Student.school_name)

# print("----------------------")

print("Student List:")
for student in Student.student_list:
    print(f"ID: {student.student_id}, Name: {student.name}, School: {Student.school_name}")
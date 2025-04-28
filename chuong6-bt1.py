# list_in = [1,4,5,38,93,54,23]

# list_out=[x+6 for x in list_in]

# print(list_out)







# list_in = [1,4,5,38,93,54,23]

# list_out=[x**2  for x in list_in if x**2>50]

# print(list_out)








# list_in = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

# list_out = [x for x in list_in if len(x) > 5]

# list_out = [x for x in list_in if 'a' in x]

# list_out =[x for x in list_in if x.count('a')>2]

# list_out=[x.capitalize() for x in list_in if 'a' in x and len(x)>5]

# print(list_out)


list_in = [1,2,3,4,5,6]
list_out =[x for x in list_in if x %2 ==0]
print(list_out)


# # Danh sách màu sắc và giá trị
# colors = ['C', 'R', 'CH', 'B']
# atts = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# # Tạo danh sách các lá bài
# deck = [f"{att}{color}" for color in colors for att in atts]

# print(deck)
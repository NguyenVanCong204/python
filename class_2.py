# list_a = [10,20,30,40]

# for idx,item in enumerate(list_a) :
#     print(f'value of each item #{idx+1} : {item}')


#################################


# list_input = [1,2,3,4]

# list_output=[]
# #Lấy phần tử số chẵn và bỏ vào list_output
# for item in list_input:
#     if item % 2 == 0:
#         list_output.append(item)   
# print(list_output)


#################################

# list_input = [10,20,30,20,10,50,60,40,80,50,40]

# list_output=[]

# for item1 in list_input:
#     if item1 not in list_output:
#         list_output.append(item1)
# list_output.sort()
# print(list_output)

#################################

list_a = ['a', 'b']
n = 5  

for i in range(1, n + 1):  
    for item in list_a:  
        print(f'{item}{i}')  

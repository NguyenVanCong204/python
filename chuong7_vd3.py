# my_list = ["gaeks", "geeg", "keek", "practice", "aa"]
# list_new = list(filter(lambda a: a==a[::-1] , my_list))
# print(list_new)


# my_list = ["gaeks", "geeg", "keek", "practice", "aa"]
# list_new = list(filter(lambda a: all(i in a for i in "egsk") , my_list))
# print(list_new)


# l1 = [4, 2, 13, 21, 5]
# list_new = list(map(lambda a: a*2 , l1))
# print(list_new)

# numbers = [1, 2, 3, 4]
# list_new = list(map(lambda a: a*a if a%2==0 else a*2 , numbers))
# print(list_new)



nums1 = [1, 2, 3]
nums2 = [4, 5, 6]

list_new = list(map(lambda x,y: x+y  , nums1,nums2))
print(list_new)
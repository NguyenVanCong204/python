def addition(n):
    if n%2==0:
         return n*n
    
    else :
        return n*2
    

numbers = [1, 2, 3, 4]
result = map(addition, numbers)
print(list(result))

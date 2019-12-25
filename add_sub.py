def add_sub(x,y):
    c= x+y
    d= x-y
    return c,d

a = int(input("Please enter value 1:"))
b = int(input("Please enter value 2:"))
result1,result2 = add_sub(a,b)
print("Addition is:",result1)
print("Subtraction is:",result2)


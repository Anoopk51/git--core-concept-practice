
def func(num1,num2):
    return num1+num2
num1 = 4
num2 = 3    
a=func(num1,num2)
print(a)


# def product(l):
#     for i in l:
#         a =list(lambda  i: i**2)

l = [1,2,3,4,5]
# for i in l:
a=list(map(lambda i: i ** 2,l))
print(a)

print(l)
# print(product(l))



# x = lambda a,b : a+b
# print(x(3,4))
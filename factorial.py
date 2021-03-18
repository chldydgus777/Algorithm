def factorial(num):
    if num <= 1:
        return 1
    return factorial(num-1)*num

#          f(4)*5
#       f(3)*4*5
#    f(2)*3*4*5
# f(1)*2*3*4*5
#  1 *2*3*4*5
print(factorial(5))

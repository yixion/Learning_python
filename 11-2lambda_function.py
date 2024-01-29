'''
    lambda function:https://www.freecodecamp.org/news/python-lambda-function-explained/
    Lambda functions are similar to user-defined functions but without a name.
    They're commonly referred to as anonymous functions.
'''
#create lambda function
#lambda argument(s) : expression
'''
    the anonymous function will automatically return the result of 
    the expression in the function once it is executed.
'''
#normal one
def power_x(x):
    return x*x
print(power_x(3))
#lambda function
print((lambda x: x * x)(3))

#when use
'''
    You should use the lambda function to create simple expressions. 
    For example, expressions that do not include complex structures 
    such as if-else, for-loops, and so on.
'''
#可以和iterable的function搭配使用
#filter()
number_list = [1, 2, 3, 4, 5, 6]
b = filter(lambda x:x%2==0,number_list)
print(list(b))
#map
c = map(lambda x:pow(x, 2), number_list)
print(list(c))
#sort
a = [[1,2],[4,3],[5,1],[9,2],[3,7]]
d = sorted(a, key=lambda x:x[1])
print(d)
'''
Variable
Python 裡的變數，表示的是「某個物件」的「名稱」，當給予某個變數內容時，
其實是將內容放入一個物件「容器」中儲存，然後「給予這個物件一個變數名稱」。
'''

#string
name = "Michael" 
print(name)
print(type(name))
#integer
number = 1
print(number)
print(type(number))
#float
float = 1.0
print(float)
print(type(float))
#boolean
boo = True
print(boo)
print(type(boo))

'''
Python — Mutable vs Immutable:https://medium.com/starbugs/python-mutable-%E8%88%87-immutable-8ef7804181cd
string tuple, float, and integer is immutable
dictionary is mutable
變數的運作原理: https://medium.com/starbugs/python-%E4%B8%80%E6%AC%A1%E6%90%9E%E6%87%82-pass-by-value-pass-by-reference-%E8%88%87-pass-by-sharing-1873a2c6ac46
***Pass by Assignment***
'''
a = 2
b = c = a
print(f"a:{a}, b:{b}, c:{c}")
'''
a=2
c=3
b = c = a
result ?
'''
#可以用逗號同時宣告不同變數不同值，也可以交換數值
a, b, c = 1, 2, 3
print(f"a:{a}, b:{b}, c:{c}")
#同時輸出字串和變數:https://blog.csdn.net/zag666/article/details/123131981
a, b, c = c, b, a
print(f"change the number:a:{a}, b:{b}, c:{c}")
#name a variable in code:https://www.w3schools.com/python/python_variables_names.asp


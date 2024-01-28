'''
    當你的code變得越來越肥的時候，你就會需要將重複或是有特別定義的程式，拆分出來，
    The is so called function.
'''
#define function, add variable in it
#可以有多個variable，且也可以使用關鍵字引數
def hello(msg):
    print(f"Hello world!{msg}")
hello(" 55555")
#return value
#可以回傳多個variable，但需要給予相對應的variable，不然會出錯
#只賦予一個值會變成tuple
def plus(number1, number2):
    return number1 + number2
sum = plus(4, 5)
print(sum)
#函式內定義的函式只有內部可以取用，且內部變數式區域變數(可能造成namespace的重疊)
def minus():
    number1 = 1
    def h1():
        nonlocal number1 #use nonlocal to solve the problem
        number1 = number1 + 1
        print(number1)
    h1()
minus()
#variable如果是*args or **kwargs會對傳入的資料造成型態的改變
#*args會變成tuple
def input_data(*args):
    print(args)
    print(type(args))
input_data(1,2,3,'a','b','c')
#**kwargs會變成dictionary
def input_data2(**kwargs):
    print(kwargs)
    print(type(kwargs))
input_data2(name='hisf', age=18, like='book')
#use pass do nothing
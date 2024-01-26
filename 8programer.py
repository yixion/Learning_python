# if-else 三元運算式
number1 = 2
number2 = 5
string3 = 'Hi' if number1<number2 else 'fuck'
print(string3)

#and or not 
number3 = 1
if number1 > number2 or number3< number1:
    print("hello world")

#for and while loop
for i in [1, 2, 3, 4, 5]:
    print(i)
for i in range(1,10,2):
    print(i)
j = 10
while j>0:
    j -= 1
    print(f"j={j}")

#try except
try:
    a = input('輸入數字:')
    print(a+1)
except NameError:
    print('使用沒有被定義的對象')
#使用錯誤訊息:https://steam.oxxostudio.tw/category/python/basic/try-except.html#a2
except TypeError:
    print('型別發生錯誤')
except Exception as e:#可以將錯誤資訊印出來
    print(e)
print('Hello')
#raise assert
#raise 可以強制丟出錯誤訊息
try:
    input_data = int(input("please enter number 0~9"))
    if(input_data>9 or input_data<0):
        #raise 
        # or use assert
        assert False, "number is not in the range"
    print(input_data)
except AssertionError as msg:
    print(msg)
except:
    print("You enter the wrong error")
#else 和 finally 是在except外的兩個額外判斷式
#else 完全沒有錯誤，沒有執行except才會執行
#finally 不管有沒有錯都會執行該區塊的程式



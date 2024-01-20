'''
    「數字」就是我們常見的阿拉伯數字，但在 Python 裡，數字又分成「整數」、「浮點數」( 小數 ) 
    和「底數」，數字可以進行各種數學式的運算，也可以進行各種邏輯比較、時間表達等以數字為主的運算。
'''
print(type(5))
#加法
variable1 = 4
variable2 = 5
print(variable1 + variable2)
#減法
variable1 = 4
variable2 = 5
print(variable1 - variable2)
#乘法
variable1 = 4
variable2 = 5
print(variable1 * variable2)
#除法
variable1 = 4
variable2 = 5
print(variable1 / variable2) #integer change to float
#除法取整數
variable1 = 10
variable2 = 4
print(variable1 // variable2)
#除法取餘數
variable1 = 4
variable2 = 5
print(variable1 % variable2)
#次方
variable1 = 2
variable2 = 3
print(variable1 ** variable2)
#型態函式轉換
integer = int(9/2) #float change to integer
print(integer)
print(int('101', 2))  # 5   二進制
print(int('101', 8))  # 65  八進制
print(int('101', 16)) # 257 十六進制
0b1111 # 15 ( 二進制 ) or 0B
0o1111 # 585 ( 八進制 ) or 0O
0x1111 # 4369 ( 十六進制 ) or 0X
'''
「布林 Bool」只有 True 和 False 兩個值，通常 True 可以表示為 1，Fasle 可以表示為 0
'''
if True:
    print("This is true")
if False:
    print("This is false")
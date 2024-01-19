'''
    global value 全域變數
    local value 區域變數
    block value(c language) 區塊變數:https://openhome.cc/Gossip/CGossip/Scope.html
'''
'''
在 Python 裡的主程式與每個函式，都有各自的名稱空間 ( namespace )，簡單的區分規則如下：
    1.主程式定義「全域」的名稱空間，在主程式定義的變數是「全域變數」。
    2.個別函式定義「區域」的名稱空間，個別函式裡定義的變數就是「區域變數」。
    3.每個名稱空間裡的變數名稱都是「唯一的」。
    4.不同名稱空間內的變數名稱可以相同，例如函式 A 可以定義 a 變數，函式 B 也可以定義 a 變數，兩個 a 變數是完全不同的變數。
'''
'''
    Built-in scopes 內置預設名稱空間(預設的函數名稱)
    Global Namespace 全域名稱空間
    Local Namespace 區域名稱空間
'''
variable = 5
def function():
    variable = 4  #if this line disapear?
    print(variable)
    print(variable + 1)
function()
print(variable)

def function2():
    global variable #可以讓local value變成global value
    variable = 0
function2()
print(variable)
'''
    當多個變數同時指向一個串列、字典或集合時，只要變數內容被
    修改 ( 並非使用等號賦值 )，不論這個變數是全域還是區域變
    數，另外一個變數內容也會跟著更動
'''
a = []
b = a
c = []
d = c

def f1():
    # global c        # 如果加上這行，f2 裡的 c 就會被影響
    a.append(1)
    c = [1]
    print(a)  # [1]
    print(b)  # [1]   # 被影響
    print(c)  # [1]
    print(d)  # []    # 不受影響

def f2():
    print(a)  # [1]   # 被影響
    print(b)  # [1]   # 被影響
    print(c)  # []    # 不受影響，但如果 f1 加上 global c，此處就會被影響
    print(d)  # []    # 不受影響

f1()
f2()
'''
globals()：回傳一個字典，內容是「全域名稱空間」的內容。
locals()：回傳一個字典，內容是「區域名稱空間」的內容。

'''
def function3():
    local_value = 3
    print(locals())
function3()
print(globals())
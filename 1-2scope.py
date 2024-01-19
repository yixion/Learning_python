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

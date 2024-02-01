'''
一、常用的字串操作
    1.轉換與建立字串:str(x)
    2.結合字串:+
    3.重複字串:＊
    4.取出字元:str[]
    5.取得字串長度:len()
    6.將字串中的 x 替換為 y，n 為要替換的數量，可不填 ( 表示全部替換 ):str.replace(x,y,n)
    7.去除字串開頭或結尾的某些字元:str.strip()
    8.將字串字首變成大寫:str.capitalize()
    9.將字串全部轉成小寫:str.lower() & str.casefold()
    10.將字串全部轉成大寫:str.upper()
    11.將字串的大小寫對調:str.swapase()
    12.將字串全部轉成標題 ( 每個單字字首大寫 ):str.title()
    13.將序列結合成字串:str.join(itr)
    14.計算某段文字在字串中出現的次數 ( start、end 為範圍，可不填 ):str.count(sub,start,end)
    15.尋找某段文字在字串中出現的位置 ( start、end 為範圍，可不填 ):str.index(sub,start,end)
    16.格式化字串:str.format
    17.字串編碼:str.encode(encoding='utf-8',errors='strict')
二、常用的判斷方法
    1.判斷字串中是否出存在某段文字，回傳 True 或 False:sub in str
    2.判斷字串中是否都是英文字母或數字 ( 不能包含空白或符號 )，回傳 True 或 False:str.isalnum()
    3.判斷字串中是否都是英文字母 ( 不能包含數字、空白或符號 )，回傳 True 或 False:str.isalpha()
    4.判斷字串中是否都是數字 ( 不能包含英文、空白或符號 )，回傳 True 或 False:str.isdigit()
    5.判斷字串中是否都是小寫英文字母，回傳 True 或 False:str.islower()
    6.判斷字串中是否都是大寫英文字母，回傳 True 或 False:str.isupper()
    7.判斷字串中是否為標題 ( 每個單字字首大寫 )，回傳 True 或 False:str.istitle()

'''
#1~11都在3-1學過，只有8和9還沒介紹完全
#8.將字串字首變成大寫
string1 = "hello world!"
print(string1.capitalize())
#將字串全部轉成大寫
string2 = string1.upper()
print(string2)
#將字串全部轉成小寫
string2 = string2.casefold()
print(string2)
#將序列結合成字串:str.join(itr)
string3 = string2.split()
print(string3)
string3 = ','.join(string3)
print(string3)
#14計算某段文字在字串中出現的次數 ( start、end 為範圍，可不填 ):str.count(sub,start,end)
number_str = string1.count('l')
print(number_str)
number_str = string1.count('l', 0, 4)
print(number_str)
#15尋找某段文字在字串中出現的位置 ( start、end 為範圍，可不填 ):str.index(sub,start,end)
place_str = string1.index('l',4)
print(place_str)
#17.字串編碼:str.encode(encoding='utf-8',errors='strict')
'''
1.encoding default is UTF-8
2.error:
    'backslashreplace': uses a backslash instead of the character that could not be encoded
    'ignore': ignores the characters that cannot be encoded
    'namereplace': replaces the character with a text explaining the character
    'strict': Default, raises an error on failure
    'replace': replaces the character with a questionmark
    'xmlcharrefreplace': replaces the character with an xml character
'''
str = string1 + 'Ståle'
str = str.encode(encoding='ascii', errors='replace')
print(str)

#二、常用的判斷方法
#1.判斷字串中是否出存在某段文字，回傳 True 或 False:sub in str
print('l' in string1)
#2.判斷字串中是否都是英文字母或數字 ( 不能包含空白或符號 )，回傳 True 或 False:str.isalnum()
print(string1.isalnum())
#3.判斷字串中是否都是英文字母 ( 不能包含數字、空白或符號 )，回傳 True 或 False:str.isalpha()
print(string1.isalpha())
#判斷字串中是否都是數字 ( 不能包含英文、空白或符號 )，回傳 True 或 False:str.isdigit()
number = '1245'
print(number.isdigit())
#判斷字串是否為大小寫字母
new_string = 'Hee'
print(new_string.isupper())
print(new_string.islower())
print(new_string.istitle())
#why we need to know how to deel with string
#https://nadeauinnovations.com/post/2020/11/python-tricks-replace-all-non-alphanumeric-characters-in-a-string/


#what is string
print("hello")
print('hello')

#how to print the character ' you can use ""
print("'")

#you can print " the same way
print('"')

#print the article use """
print("""Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

You can display a string literal with the print() function:""")

#change different data type to string
string = str(123)
print(type(string))

#Escape Character跳脫字元:https://stackoverflow.com/a/3098328
print('\'') #single quote
print("\"") #double quote
print("\\") #Blackslash 路徑的時候就可以用到
print("1. Hello\nworld!") #New Line
print("Hello\rabc!") #Carriage Return 回到第一個character用後面的字取代
print("3. hello\tworld!") #Tab
print("4. Hello \bworld!") #Backspace
print("5.Hello \fworld!") #	Form Feed.

#add r in front of string
print(r"Hello world!\n")

#結合字串，加號可以對變數字串做結合，單純的自於字串後面，只能是字串不能是變數
string1 = "Hello "
string2 = "world!"
print(string1 + string2 + "!!!!!!")

#重複印製字串
print("hi "*3)

#取得字串長度
print(len("Apex"))

#取得字串中的字元
string3 = "League of Legend"
print(string3[0])
print(string3[-1])
#[start:end:step]可以取一個range
print(string3[0:5:2])

#大小寫
print(string3.title()) #單字字首字母變大寫
print(string3.upper()) #所有字母變大寫
print(string3.lower()) #所有字母變小寫
print(string3.swapcase()) #單字字母的大小寫對調

#分隔字串 string.split(separator, maxsplit):https://www.freecodecamp.org/chinese/news/how-to-split-a-string-in-python/
string4 = string3.split(' ')
print(string4)
print(type(string4))

#替換 string.replace(old_text, new_text, count):https://www.freecodecamp.org/chinese/news/python-string-replace-function-in-python-for-substring-substitution/
string5 = string3.replace('L', 'A')
print(string5)
string5 = string3.replace('L', 'A', 1)
print(string5)

#剝除str.strip([chars]):https://www.runoob.com/python/att-string-strip.html
string6 = string3.strip("Ld") #刪除開頭跟結尾的char
print(string6)
string6 = string3.lstrip("L") #刪除開頭的char
print(string6)
string6 = string3.rstrip("Ld") #刪除結尾的char
print(string6)






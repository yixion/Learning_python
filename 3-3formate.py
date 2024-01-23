# first way:use %
string1 = "Hello I am %s"
print(string1 % 'student')
#%後面接什麼取決於你的資料型態
'''
    %s:字串
    %d:十進制整數
    %x:十六進制整數
    %o:八進制整數
    %b:二進制整數
    %f:十進制浮點數
    %e:指數浮點數
    %g:十進制或指數浮點數
    %%:常值 %
'''

#second way format
string2 = "I'm {} ages, and I study in {}"
string3 = string2.format('12', 'high school')
print(string3)
#you can also change the order
string2 = "I'm {1} ages, and I study in {0}"
string3 = string2.format('12', 'high school')
print(string3)
#give the name
string2 = "I'm {age} ages, and I study in {school}"
string3 = string2.format(age = '12', school = 'high school')
print(string3)
#give the dictionary
string2 = "I'm {0[x][a]} ages, and I study in {0[x][s]}"
string3 = {'x':{'a':'12', 's':'school'}}
print(string2.format(string3))
#use : can control the format
string2 = "I'm {:<10s} ages, and I study in {}"
string3 = string2.format('12', 'high school')
print(string3)
string2 = "I'm {:>10s} ages, and I study in {}"
string3 = string2.format('12', 'high school')
print(string3)
string2 = "I'm {:-<10s} ages, and I study in {}"
string3 = string2.format('12', 'high school')
print(string3)

#Third way f-string 1-1的時候有用過
string1 = '12'
string2 = 'high school'
print(f"I'm {string1:->10s} ages, and I study in {string2}")

for i in range(0,101):
    print(f'{i:0<3d}',end = ' , ')
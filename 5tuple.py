'''
tuple
    特性:
        1.Iterable(可迭代的)
        2.Unmodifiable(不可修改的)
    好處:
        1.讀取速度比list快
        2.佔用的空間比較少
        3.資料更安全(因為無法修改)
    
'''

#construct tuples
ages = (12, 25, 50, 100)
print("construct tuple")
print(type(ages))
ages2 = 12, 25, 50, 100 # ','預設為tuple，只有一個資料的時候，後面加逗號也是tuple
print(type(ages2))
print(ages)
print(ages2,"\n")
ages3 = tuple([12, 25, 50, 100])# Iterative way
print(ages3)
#*也可用來放入重複的元素

#存取tuples元素的方法
#use offset
print(ages[0])
#use slice
print(ages[0:2])    
#use loop
for age in ages:
    print(age)

#search element in tuples
print(ages.index(50))
if 30 in ages:
    print(ages.index(30))
else:
    print("30 is not in the ages")
print(ages.count(30))
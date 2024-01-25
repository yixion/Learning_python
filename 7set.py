'''
    set是沒有value的dictionary，且element不會重複
'''
#build set
set1 = {0, 1, 1, 3}
print(set1)

#add element to set
set1.add(5)
print(set1)

#delete element in set
set1.remove(0)
print(set1)
set1.discard(1)
print(set1)#This won't sent the error message

#交集、連集、差集、對稱差集
a = {1,2,3,4,5}
b = {3,4,5,6,7}
print(f"交集:\n{a.intersection(b)}")
print(a&b)
print(f"聯集:\n{a.union(b)}")
print(a|b)
print(f"差集\n{a.difference(b)}")
print(a-b)
print(f"對稱差集\n{a.symmetric_difference(b)}")
print(a^b)
#確認b是否是a的子集合
c = {3, 4}
print(b.issubset(a))
print(c.issubset(b))

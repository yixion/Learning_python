'''
    list
    Three way to construct the list:
    「中括號 ( 方括號 )」、「list()」和「split() + 字串」
'''
#中括號
Berries = ['blueberry', 'berry', 'bilberry', 'black currant', 'currant', 'mulberry']
Citrusfruit = ['orange', 'blood orange', 'ponkan', 'pomelo', 'sunkist']
number = [1, 2, 3]
sumarize = [Berries, Citrusfruit, number]
print(type(sumarize))
print(sumarize)
#str.split('分割符號')
#string常用技巧已經學過
'''
    合併串列
    1.'+'
    2.extend()
'''
# 1.'+'
sumarize = Berries + Citrusfruit
print(sumarize)
# 2.extend()，extend沒有回傳直，直接改變陣列
sumarize.extend(number)
print(sumarize)

'''
    讀取list
    1.offset
    2.slice()
'''
# 1.offset
print(Berries[0])
# 2.slice()
print(Berries[:2])
print(number[::2])

'''
    Some basic skill of list
'''
# copy list
# use =
number2 = number
del(number[1])
print(number2)
number = [1,2,3]
#use slice
number2 = number[:]
del(number[1])
print(number2)

# change list 
# use offset
Kernelfruits = ["bell fruit", "start fruit", "guava", "pear", "passion fruit"]
Kernelfruits[0] = "pineapple"
print(Kernelfruits)
# use slice 只要是可迭代的的資料型別都可以用slice()
Kernelfruits[0:3] = ["watermelon", 'cantaloupe', 'muskmelon']
print(Kernelfruits)

#append(): 函式可以將項目添加在一個串列的尾端，可以是list可以存的任何資料型態
Kernelfruits.append(100)
print(type(Kernelfruits[5]))
print(Kernelfruits[5])

#insert(): 使用 insert() 函式，就可以將指定的內容，從指定的位置加入
Kernelfruits.insert(3,"Hi")
print(Kernelfruits)

#刪除資料
# 1.del(): 使用「del list(offset)」來刪除指定的項目
del Kernelfruits[3]
print(Kernelfruits)
# 2.remove(): 可以使用 remove(項目內容) 刪除該項目，如果有多個同樣內容的項目，remove() 只會刪除第一個找到的項目。
Kernelfruits.remove('watermelon')
print(Kernelfruits)
# 3.pop(): 使用的方式為「pop(offset)」，如果不指定數值或數值為 -1，則會取出最後一個項目
Kernelfruits.pop()
print(Kernelfruits)
# 4.clear(): 函式會清空整個串列的內容，使其變成一個空的串列。
Kernelfruits.clear()
print(Kernelfruits)






'''
    dictionary
    有key和value，收尋key找到相對應的value

'''
data = {'name':"林逸驤", 'age':21, 'eat':['pear', 'watermelon']}
print(type(data))
#用dict()可以將二維的資料變成dictionary
two_dimention = [['age', 12],['name', '林逸驤']]
two_dimention = dict(two_dimention)
print(type(two_dimention))
print(two_dimention)

#讀取dictionary
#use offset
print(data['name'])
print(data['eat'][1])
#use get
print(data.get('name'))

#修改dictionary裡的data

#use offset
data['age'] = 18
print(data)
data['gender'] = 'boy'
print(data)
data.setdefault('age', 22)
print(data)

#刪除element del dictionary_name[key_name] or del diction_name delete the whole dictionary
del data['gender']
print(data)
# del data
# print(data)
data.setdefault('gender', 'boy')
pop_val = data.pop('name')
print(data)
print(pop_val)

#清空dictionary
data.clear()
print(data)

#combine the dictionary
#**use different key value; otherwise value will change
dictionary1 = {'name':"林逸驤", 'age':21, 'eat':['pear', 'watermelon']}
dictionary2 = {'gender':"boy", 'height':165, 'address':['city', 'Kelun']}
com_dictionary = {**dictionary1, **dictionary2}
print(com_dictionary)
#use update()
dictionary1.update(dictionary2)
print(dictionary1)

#取得所有的key和value
print(dictionary1.keys())
print(dictionary1.values())
print('apple' in dictionary1)

#複製dictionary，跟list一樣有shallow copy 和deep copy
dictionary3 = dictionary1.copy()
import copy
dictionary4 = copy.deepcopy(dictionary1)
del dictionary1['eat'][0]
print(dictionary3)
print("\n")
print(dictionary4)
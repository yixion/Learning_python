'''
    comprehension是用在Python的可迭代物件的生成上
'''
#list comprehension
number_list = [i+2 for i in range(1,11)]
print(number_list)
#兩層for loop 也是可以做使用
number_list2 = [i+2*j for i in range(1, 11) for j in range(0,5)]
print(number_list2)
#可以搭配 if 使用
number_list3 = [i+2*j for i in range(1, 11) for j in range(0,5) if i%10==0]
print(number_list3)
#if放在前方需要在後面加上else
number_list4 = [i+2*j if i % 10 == 0 else 0 for i in range(1, 11) for j in range(0,5)]
print(number_list4)

#dictionary comprehension
number_dict = {i: i*i for i in range(0,10)}
print(number_dict)

#set comprehension
number_set = {i for i in range(0,10)}
print(number_set)

#tuple comprehension
a = tuple(i for i in range(0,10))
print(a)
#sort、sorted: list_name.sort(reverse=..., key=... ): https://www.freecodecamp.org/chinese/news/python-sort-how-to-sort-a-list-in-python/
number_sequence = [1,4,2,3,5,4,6,8,7,9]
number_sequence.sort()
print(number_sequence)
programming_languages = ["Python", "Swift","Java", "C++", "Go", "Rust"]
programming_languages.sort(reverse=True, key=len)
print(programming_languages)
#sorted有回傳值，不會改變原list，所以要用一個list去儲存
#key 可以放function、lambda function

#反轉list
# 1.use slice
print(number_sequence)
rv_number_sequence = number_sequence[::-1]
print(rv_number_sequence)
# 2.use reverse 沒有回傳值
number_sequence.reverse()
print(number_sequence)

#copy list: https://ithelp.ithome.com.tw/articles/10221255
# 1.slice()、copy()、list()
number_sequence.reverse()
number2_sequence = number_sequence[:]
number3_sequence = number_sequence.copy()
number4_sequence = list(number_sequence)
print("\n")
print(number2_sequence)
print(number3_sequence)
print(number4_sequence)
#deep copy 當list中有可變data type就會產生不同
import copy
print("deep copy\n")
print(number_sequence)
number_sequence.append([100, 400])
number5_sequence = copy.deepcopy(number_sequence)
number_sequence[10][0] = 2
print(number_sequence)
print(number5_sequence)

# 比較串列，串列長度必須都是相同的資料型態: 「<」、「<=」、「>=」、「>」
# *可以重複list內容



'''
    物件是一種自訂的資料結構，裡面可能包含了各種變數、屬性、函式或方法
    在 Python 裡的任何東西 ( 數字、文字、函式...等 ) 都是物件
    In computer science, an object can be a variable, a data structure, 
    a function, or a method, and as such, is a value in memory referenced by an identifier.
    metaclass: https://dboyliao.medium.com/%E6%B7%BA%E8%AB%87-python-metaclass-dfacf24d6dd5
    什麼是object:region of data storage in the execution environment, the contents of 
                 which can represent values
'''
#construct class
class human():
    def __init__(self, age, weight): # 建立預設屬性，可以預設一些參數做修改
        self.eye = 2
        self.mouth = 1
        self.nose = 1
        self.age = age
        self.weight = weight
    def say(self, msg): # 建立class可以使用的函式
        print(msg)
    def play(self, sport):
        print(sport)
    def mouth_number(self):
        print(f"I have {self.mouth} mouth")
    def human_age(self):
        print(f"My age is {self.age}")  
'''
    self 這個參數，這個參數代表「透過類別建立的物件本體」，
    使用 self 可以讀取到這個物件的所有屬性
'''
a = human(18, 70)
b = human(20, 60)
a.mouth_number()
a.human_age()
b.human_age()
#從外部修物件屬性會覆蓋原本的屬性
#@property:https://www.maxlist.xyz/2019/12/25/python-property/
#@property 是要實現物件導向中設計中封裝的實現方式
a = human(18, 70)
print(type(a))
print(type(human))
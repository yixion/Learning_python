class Cat:
    #可以把屬性寫在init外面，例如這裡
    foot = 4
    def __init__(self): #屬性
        self.eyes = 2
        self.hungry = False
    def eat(self, food):
        self.hungry = True
        print(f"Thanks for give me {food}!")
Andy = Cat() #instance of cat class
Andy.eat("fish") #call the method
Andy.tail = 1 #在外面添加屬性
print(Andy.eyes) #呼叫屬性
print(Andy.foot)
print(Andy.tail)

class Lion(Cat):
    def __init__(self):
        super().__init__()
        self.mouth = 1
    def eat(self):
        print("覆蓋")
        self.__sleep()
    def __sleep(self):
        print("I am sleeping")
Waston = Lion()
print(Waston.foot)
Andy.eat("fish")
Waston.eat()
# Waston.__sleep()
class dog:
    def __init__(self):
        self.lag = 4
    @property#讓以下method唯讀，不能修改
    def eat(self):
        print("snoop said: hi")
snoop = dog()
Waston.eat()
snoop.eat()


Humans = []
class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def hello(self):
        return f"こんにちは私の名前は{self.name}です。年齢は{self.age}歳です。"
x= int(input())
for i in range(x):
    name = input()
    age = int(input())
Humans.append(Human(name, age))
for i in Humans:
    print(i.hello())
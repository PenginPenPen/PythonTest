class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def describe(self):
        print(f"名前:{self.name},年齢{self.age}")
x = int(input())
animals = []
for i in range(x):
    name = input()
    age = int(input())
    animals.append(Animal(name,age))
for anim in animals:
    anim.describe()

def checkage(animal):
    name = animal.name
    if animal.age >= 7:
        print(f"{animal.name}は年長です")
    else:
        print(f"{animal.name}は若いです")

for anim in animals:
    checkage(anim)
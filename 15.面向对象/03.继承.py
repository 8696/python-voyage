# 继承

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def __speak(self):
        print("Animal is speaking.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing.")

dog = Dog("Rufus")
dog.eat()
dog.bark()

cat = Cat("Whiskers")
cat.eat()
cat.meow()  
# cat.__speak()  # 'Cat' object has no attribute '__speak'
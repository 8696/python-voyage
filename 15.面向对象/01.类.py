# 类
class Person:
    name = "Mary"
    age = 18
    __weight = 0

    def __init__(self, name, age, weight):
        print('构造函数被调用')
        self.name = name
        self.age = age
        self.__weight = weight

    def say_hello(self):
        print("Hello, my name is {} and I am {} years old.".format(self.name, self.age))
        print("My weight is {} kg.".format(self.__weight))

    def get_weight(p):
        return p.__weight

    def set_weight(p, weight):
        p.__weight = weight

    def get_age(p):
        return p.age

p1 = Person("Alice", 25, 50)

p1.say_hello()

# 访问实例属性
print(p1.name) # Alice

# 访问类属性
print(Person.name) # Mary

# 修改类属性
Person.name = "Tom"
print(Person.name) # Tom

# 访问实例属性
print(p1.name) # 还是 Alice

# 实例属性优先级高于类属性
p1.name = "Bob"
print(p1.name) # Bob


# 获取 weight 属性
print(p1.get_weight()) # 50

# 访问私有属性
# print(p1.__weight) # 'Person' object has no attribute 'weight'

# 修改私有属性
# p1.__weight = 60 # AttributeError: 'Person' object has no attribute '__weight'

# 访问你不存在类属性
# print(Person.last_name) type object 'Person' has no attribute 'last_name'

# 类方法
Person.age = 20
print(Person.get_age(Person)) # 20
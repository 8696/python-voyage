class Person:
    name = 'Mary'
    age = 18

    def __init__(self, name, age):
        self.name = name
        self.age = age
  
    @staticmethod
    def set_name(value):
        Person.name = value

    @staticmethod
    def get_name():
        return Person.name
    
    @classmethod
    def set_age(cls, value):
        cls.age = value

    @classmethod
    def get_age(cls):
        return cls.age

# 调用静态方法
Person.set_name('Tom')
print(Person.get_name()) # output: Tom

# 实例化对象
p = Person('Jenny',30)
print(p.name) # output: Jenny
print(p.age) # output: 30


# 调用实例方法，但是该方法设置的是类属性，而不是实例属性
p.set_name('Jane')
print(p.get_name()) # output: Jane


# 调用实例方法，该方法设置的是实例属性
p.set_age(35)
print(p.get_age()) # output: 35
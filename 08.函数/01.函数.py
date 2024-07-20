# 定义一个普通函数
def say_hello():
    print("Hello, world!")   # 函数体 

 
# 调用函数
say_hello()   # 输出 "Hello, world!"


# 定义一个带参数的函数
def greet(name):
    print("Hello, " + name + "!")   # 函数体 


# 调用带参数的函数
greet("Alice")   # 输出 "Hello, Alice!"



# 定义一个带默认参数的函数
def greet_default(name="world"):
    print("Hello, " + name + "!")   # 函数体 


# 调用带默认参数的函数
greet_default()   # 输出 "Hello, world!"
greet_default("Alice")   # 输出 "Hello, Alice!"


# 定义一个带多个参数的函数
def add(x, y):
    return x + y   # 函数体 


# 调用带多个参数的函数
result = add(2, 3)   # 输出 5 
print(result)   # 输出 5  


# 定义一个带可变参数的函数
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result   # 函数体 


# 调用带可变参数的函数
result = add_many(1, 2, 3, 4, 5)   # 输出 15 
print(result)   # 输出 15   


# 关键字参数
def person(name, age):
    print("Name:", name)
    print("Age:", age)


# 调用关键字参数的函数
person(age =25, name="Alice")   #   "Name: Alice"  "Age: 25"


# 可变对象参数
def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4])
   print ("函数内取值: ", mylist) # [10, 20, 30, [1, 2, 3, 4]]
   return
 
# 调用changeme函数
mylist = [10,20,30]
changeme( mylist )
print ("函数外取值: ", mylist) # [10, 20, 30, [1, 2, 3, 4]]



# return 语句
def add_and_mul(x, y):
    return x + y, x * y   # 函数体 


# 调用带 return 语句的函数
result1, result2 = add_and_mul(2, 3)   # 输出 (5, 6) 
print(result1)   # 输出 5 
print(result2)   # 输出 6  


# 递归函数
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)   # 函数体 


# 调用递归函数
result = factorial(5)   # 输出 120 
print(result)   # 输出 120  


# 匿名函数
add = lambda x, y: x + y   # 匿名函数
result = add(2, 3)   # 输出 5 
print(result)   # 输出 5  








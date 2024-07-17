# bool 布尔类型
# Python 中一种基本的数据类型，它只有两个值：True 和 False。

# 布尔类型可以用 and、or、not 运算符进行逻辑运算。

# 1. 布尔运算符
# and 运算符：
# 两个布尔值都为 True，则结果为 True，否则为 False。
# 语法：a and b


# or 运算符：
# 两个布尔值中只要有一个为 True，则结果为 True，否则为 False。
# 语法：a or b


# not 运算符：      
# 布尔值取反，True 变为 False，False 变为 True。
# 语法：not a


# 2. 布尔值操作
# 布尔值可以进行逻辑运算，也可以进行布尔值操作。      
# 布尔值操作包括：比较运算、逻辑运算、布尔值操作符。

# 3. 布尔值比较
# 布尔值比较可以用 ==、!=、is、is not 运算符进行。
# 语法：a == b   # a 等于 b
# 语法：a!= b   # a 不等于 b
# 语法：a is b   # a 与 b 是同一个对象    
# 语法：a is not b   # a 与 b 不是同一个对象


# 4. 布尔值逻辑运算
# 布尔值逻辑运算可以用 and、or、not 运算符进行。
# 语法：a and b   # 只有 a 和 b 都为 True，结果才为 True
# 语法：a or b    # 只要 a 或 b 为 True，结果就为 True
# 语法：not a     # 布尔值取反，True 变为 False，False 变为 True


# 5. 布尔值操作符
# 布尔值操作符包括：
# 1）布尔值取反：not a
# 2）布尔值与：a and b
# 3）布尔值或：a or b
# 4）布尔值非：not a
# 5）布尔值比较：a == b、a!= b、a is b、a is not b    

# 布尔类型的值和类型
a = True
b = False
print(type(a))  # <class 'bool'>
print(type(b))  # <class 'bool'>

# 布尔类型的整数表现
print(int(True))   # 1
print(int(False))  # 0

# 使用 bool() 函数进行转换
print(bool(0))         # False
print(bool(42))        # True
print(bool(''))        # False
print(bool('Python'))  # True
print(bool([]))        # False
print(bool([1, 2, 3])) # True

# 布尔逻辑运算
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

# 布尔比较运算
print(5 > 3)  # True
print(2 == 2) # True
print(7 < 4)  # False

# 布尔值在控制流中的应用
if True:
    print("This will always print")
    
if not False:
    print("This will also always print")
    
x = 10
if x:
    print("x is non-zero and thus True in a boolean context")
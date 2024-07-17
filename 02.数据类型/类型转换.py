# 类型转换

# 隐式类型转换
# 1. 算术运算符：整数和浮点数相加，结果为浮点数
int_val = 10
float_val = 3.14
print(int_val + float_val)  # 13.14

# 2. 字符串拼接：整数和字符串相加，结果为字符串
str_val = "hello"
int_val = 10
print(str_val + str(int_val))  # hello10

# 3. 布尔值运算：布尔值不能参与算术运算，但可以与其他类型进行比较
bool_val = True
int_val = 10
print(bool_val and int_val)  # 10

# 4. 列表、元组、集合、字典等容器：不能参与算术运算，但可以与其他类型进行比较
list_val = [1, 2, 3]
int_val = 10
print(list_val + [int_val])  # [1, 2, 3, 10]  

# 5. 其他类型：不能参与算术运算，不能与其他类型进行比较
str_val = "hello"
int_val = 10
# print(str_val + int_val)  # TypeError: can only concatenate str (not "int") to str

# 显式类型转换
# 1. int()：将其他类型转换为整数

int_val = int("10")
float_val = float("3.14")
print(int_val + float_val)  # 13

# 2. float()：将其他类型转换为浮点数

int_val = 10
str_val = "3.14"
print(float(int_val) + float(str_val))  # 13.14

# 3. str()：将其他类型转换为字符串

int_val = 10
float_val = 3.14
print(str(int_val) + str(float_val))  # 103.14

# 4. bool()：将其他类型转换为布尔值

int_val = 10
bool_val = bool(int_val)
print(bool_val)  # True

# 5. list()：将其他类型转换为列表

str_val = "hello"
int_val = 10
print(list(str_val) + [int_val])  # ['h', 'e', 'l', 'l', 'o', 10]

# 6. tuple()：将其他类型转换为元组

str_val = "hello"
int_val = 10
print(tuple(str_val) + (int_val,))  # ('h', 'e', 'l', 'l', 'o', 10)

# 7. set()：将其他类型转换为集合

str_val = "hello"
int_val = 10
print(set(str_val) | {int_val})  # {'l', 'h', 'o', 10}

# 8. dict()：将其他类型转换为字典

str_val = "hello"
int_val = 10
print(dict(zip(str_val, range(len(str_val)))) | {"int_val": int_val})  # {'h': 0, 'e': 1, 'l': 2, 'o': 3, 'int_val': 10}


# 9. complex()：将其他类型转换为复数

int_val = 10
float_val = 3.14
print(complex(int_val, float_val))  # (10+3.14j)  

# 10. bytes()：将其他类型转换为字节串

str_val = "hello"
print(bytes(str_val, encoding="utf-8"))  # b'hello'

# 11. bytearray()：将其他类型转换为字节数组


str_val = "hello"
print(bytearray(str_val, encoding="utf-8"))  # bytearray(b'hello')


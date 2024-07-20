# for循环的基本用法
# 可迭代对象： 列表、元组、字符串、字典、集合、生成器


# 列表示例
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)   # 输出1 2 3 4 5

# 元组示例
my_tuple = (10, 20, 30)
for item in my_tuple:
    print(item)   # 输出10 20 30

# 字符串示例
my_string = "Hello"
for char in my_string:
    print(char)   # 输出H e l l o

# 字典示例（默认遍历键）
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(key)   # 输出a b c

# 集合示例
my_set = {1, 2, 3}
for item in my_set:
    print(item)   # 输出1 2 3

# 生成器示例
def my_generator():
    yield 1
    yield 2
    yield 3

for num in my_generator():
    print(num)   # 输出1 2 3




# else语句
# for循环的else语句在循环正常结束（即没有遇到break语句）时执行，循环正常结束的条件有两个：
# 1. 循环正常结束，即没有执行到break语句
# 2. 循环结束时没有遇到StopIteration异常

my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)   # 输出1 2 3 4 5  
else:
    print("循环正常结束")   # 输出循环正常结束



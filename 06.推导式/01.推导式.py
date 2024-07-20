# Python 推导式是一种独特的数据处理方式，可以从一个数据序列构建另一个新的数据序列的结构体。

# Python 推导式是一种强大且简洁的语法，适用于生成列表、字典、集合和生成器。

# 在使用推导式时，需要注意可读性，尽量保持表达式简洁，以免影响代码的可读性和可维护性。

# Python 支持各种数据结构的推导式：

# 列表(list)推导式
# 字典(dict)推导式
# 集合(set)推导式
# 元组(tuple)推导式


# 列表推导式
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']

# 筛选出名字长度大于 4 的名字 
long_names = [name for name in names if len(name) > 4]
print(long_names)  # ['alice', 'Jerry', 'Wendy', 'Smith']

# 计算 30 以内可以被 3 整除的整数
divisible_by_3 = [num for num in range(30) if num % 3 == 0]
print(divisible_by_3)  # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]



# 字典推导式

# 使用字符串及其长度创建字典
string_dict = {s: len(s) for s in ['apple', 'banana', 'orange', 'pear']}
print(string_dict)  # {'apple': 5, 'banana': 6, 'orange': 6, 'pear': 4}

# 提供三个数字，以三个数字为键，三个数字的平方为值来创建字典
num_dict = {num: num**2 for num in [1, 2, 3]}
print(num_dict)  # {1: 1, 2: 4, 3: 9}


# 集合推导式

#计算数字 1,2,3 的平方数
squares = {num**2 for num in [1, 2, 3]}
print(squares)  # {1, 4, 9}

#判断不是 abc 的字母并输出
letters = {'a', 'b', 'c', 'd', 'e'}
not_abc = {letter for letter in letters if letter != 'a' and letter != 'b' and letter != 'c'}
print(not_abc)  # {'d', 'e'}  




# 元组推导式
# 生成一个包含数字 1~9 的元组
numbers = tuple(num for num in range(1, 10))
print(numbers)  # (1, 2, 3, 4, 5, 6, 7, 8, 9)
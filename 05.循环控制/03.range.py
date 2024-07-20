# range()函数可以生成一个整数序列，可以指定起始值、终止值、步长

# 1. 基本用法
# range(stop)：生成从0开始的整数序列，直到stop-1结束，步长为1
print(list(range(5)))  # [0, 1, 2, 3, 4]

# range(start, stop)：生成从start开始的整数序列，直到stop-1结束，步长为1
print(list(range(2, 5)))  # [2, 3, 4]


# 2. 步长
# range(start, stop, step)：生成从start开始的整数序列，直到stop-1结束，步长为step
print(list(range(0, 10, 2)))  # [0, 2, 4, 6, 8]

# 步长可以是负数，表示逆序
print(list(range(10, 0, -1)))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]  

# 步长也可以为0，表示不跳过任何元素
print(list(range(0, 10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 步长也可以为负数，表示反向遍历
print(list(range(10, 0, -1)))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


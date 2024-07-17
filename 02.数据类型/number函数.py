# 数学函数
import math

# abs 函数
num1 = -10
print(f"绝对值：{abs(num1)}") # 10

# ceil 函数
num2 = 4.1
print(f"上入整数：{math.ceil(num2)}") # 5

# exp 函数
print(f"e 的 1 次幂：{math.exp(1)}") # 2.718281828459045

# fabs 函数
num3 = -10
print(f"浮点数形式的绝对值：{math.fabs(num3)}") # 10.0

# floor 函数
num4 = 4.9
print(f"下舍整数：{math.floor(num4)}") # 4

# log 函数
print(f"以 e 为底的对数：{math.log(math.e)}") # 1.0
print(f"以 10 为底 100 的对数：{math.log(100, 10)}") # 2.0

# log10 函数
print(f"以 10 为底 100 的对数：{math.log10(100)}") # 2.0

# max 和 min 函数
numbers = [5, 8, 2, 10]
print(f"最大值：{max(numbers)}")  # 10
print(f"最小值：{min(numbers)}") # 2

# modf 函数
num5 = 3.14
fractional_part, integer_part = math.modf(num5)
print(f"小数部分：{fractional_part}，整数部分：{integer_part}") # 0.14000000000000001，3

# pow 函数
print(f"2 的 3 次幂：{pow(2, 3)}") # 8

# round 函数
num6 = 3.14159
print(f"四舍五入到两位小数：{round(num6, 2)}") # 3.14

# sqrt 函数
num7 = 9
print(f"平方根：{math.sqrt(num7)}") # 3.0


# 随机数函数

import random

# choice 函数
print("choice 函数示例：") # 随机选择一个元素
seq = [1, 2, 3, 4, 5]
print(random.choice(seq)) # 随机选择一个元素
print(random.choice("hello")) # 随机选择一个字符

# randrange 函数
print("randrange 函数示例：")
print(random.randrange(10))  # 生成 0 到 9 之间的随机数
print(random.randrange(1, 10))  # 生成 1 到 9 之间的随机数
print(random.randrange(1, 10, 2))  # 生成 1 到 9 之间的奇数

# random 函数
print("random 函数示例：")
print(random.random())  # 生成 0 到 1 之间的随机浮点数

# seed 函数
print("seed 函数示例：")
random.seed(10)  # 设置种子
print(random.random())  # 每次运行结果相同

# shuffle 函数
print("shuffle 函数示例：")
lst = [1, 2, 3, 4, 5]
random.shuffle(lst)
print(lst)

# uniform 函数
print("uniform 函数示例：")
print(random.uniform(1, 5))  # 生成 1 到 5 之间的随机浮点数


# 三角函数
import math

# acos 函数
print("acos 函数示例：")
print(math.acos(0.5)) # 1.0471975511965976

# asin 函数
print("asin 函数示例：")
print(math.asin(0.5)) # 0.5235987755982988

# atan 函数
print("atan 函数示例：")
print(math.atan(1)) # 0.7853981633974483

# atan2 函数
print("atan2 函数示例：")
print(math.atan2(1, 1)) # 45.0

# cos 函数
print("cos 函数示例：") 
print(math.cos(math.pi / 2)) # 0.0

# hypot 函数
print("hypot 函数示例：") 
print(math.hypot(3, 4)) # 5.0

# sin 函数
print("sin 函数示例：")
print(math.sin(math.pi / 2)) # 1.0

# tan 函数
print("tan 函数示例：")
print(math.tan(math.pi / 4)) # 1.0
 
# degrees 函数
print("degrees 函数示例：")
print(math.degrees(math.pi / 2)) # 90.0

# radians 函数
print("radians 函数示例：")
print(math.radians(90)) # 1.5707963267948966

# 数学常量
print(math.pi)  # 圆周率
print(math.e)  # 自然常数
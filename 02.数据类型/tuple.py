# Tuple 元组 是一个有序列表，元素之间用逗号隔开，元素不能修改，元组可以作为函数的参数和返回值。

# 创建元组
t = (1, 2, 3, 4, 5)
print(t) # (1, 2, 3, 4, 5)

# 访问元组元素
print(t[0]) # 1
print(t[1:3]) # (2, 3)

# 修改元组元素 - 不支持修改元组元素
# t[0] = 10 # TypeError: 'tuple' object does not support item assignment


# 元组作为函数参数
def add(a, b):
    return a + b

print(add(t[0], t[1])) # 3

# 元组作为函数返回值
def get_tuple():
    return (1, 2, 3)

t = get_tuple()
print(t) # (1, 2, 3)  

# 注意：元组是不可变的，不能修改元素，只能重新赋值。  

# 元组的拆包
t = (1, 2, 3)
a, b, c = t
print(a, b, c) # 1 2 3  

# 元组的嵌套
t = ((1, 2), (3, 4), (5, 6))
print(t[0]) # (1, 2)
print(t[0][0]) # 1
print(t[0][1]) # 2  

# 元组的比较
t1 = (1, 2, 3)
t2 = (1, 2, 3)
t3 = (1, 2, 4)
print(t1 == t2) # True
print(t1 == t3) # False
print(t1 < t3) # True 

# 元组的运算
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(t1 + t2) # (1, 2, 3, 4, 5, 6)
print(t1 * 2) # (1, 2, 3, 1, 2, 3)
print(t1[1:]) # (2, 3)
print(t1[::-1]) # (3, 2, 1)

# 元组的遍历
t = (1, 2, 3)
for i in t:
    print(i) # 1 2 3  

# 元组的切片
t = (1, 2, 3, 4, 5)
print(t[1:3]) # (2, 3)
print(t[1:]) # (2, 3, 4, 5)
print(t[:3]) # (1, 2, 3)
print(t[::2]) # (1, 3, 5) 

# 元组的复制
t = (1, 2, 3)
t1 = t
t2 = t[:]
print(t1) # (1, 2, 3)
print(t2) # (1, 2, 3) 

# 元组的排序
t = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)
t1 = sorted(t)
print(t1) # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
t2 = sorted(t, reverse=True)
print(t2) # [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1] 

# 元组的元素个数
t = (1, 2, 3)
print(len(t)) # 3 

# 元组的元素是否存在  
t = (1, 2, 3)
print(1 in t) # True
print(4 in t) # False

# 元组的元素是否唯一
t = (1, 2, 3)
print(len(set(t)) == len(t)) # True 

# 元组的元素是否相等
t1 = (1, 2, 3)
t2 = (1, 2, 3)
t3 = (1, 2, 4)
print(t1 == t2) # True
print(t1 == t3) # False 

# 元组的元素是否为空
t = ()
print(t) # ()
print(len(t) == 0) # True 

# 元组的元素是否为元组
t = (1, 2, 3)
print(isinstance(t, tuple)) # True 

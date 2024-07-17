# Set 是一个无序不重复元素的集合。

# 创建一个空集合
s = set()

# 向集合中添加元素
s.add(1)
s.add(2)
s.add(3)
s.add(2)


# 输出集合中的元素
print(s)  # {1, 2, 3}

# 判断元素是否在集合中
print(1 in s)  # True
print(4 in s)  # False


# 集合的运算
# 并集
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(s3)  # {1, 2, 3, 4, 5}


# 交集
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1.intersection(s2)
print(s3)  # {2, 3}


# 差集
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1.difference(s2)
print(s3)  # {1}


# 对称差集
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1.symmetric_difference(s2)
print(s3)  # {1, 4}   

# 集合的更新
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s1.update(s2)
print(s1)  # {1, 2, 3, 4}


# 集合的删除
s1 = {1, 2, 3}
s1.remove(2)
print(s1)  # {1, 3}


# 清空集合
s1 = {1, 2, 3}
s1.clear()
print(s1)  # set()    

# 集合的拷贝
s1 = {1, 2, 3}
s2 = s1.copy()
print(s2)  # {1, 2, 3}


# 集合的元素个数
s1 = {1, 2, 3}
print(len(s1))  # 3

# 集合的遍历
s1 = {1, 2, 3}
for i in s1:
    print(i)  # 1 2 3 

# 集合的生成式语法
s1 = {i for i in range(1, 4)}
print(s1)  # {1, 2, 3}  

# 集合的推导式语法
s1 = {i**2 for i in range(1, 4)}
print(s1)  # {1, 4, 9}  

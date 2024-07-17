my_list = [10, 9, 8, 7, 6]

# 列表方法

# 1. append() 向列表末尾添加元素
my_list.append(11)
print(my_list)  # [10, 9, 8, 7, 6, 11] 


# 2. extend() 向列表末尾添加多个元素
my_list.extend([12, 13, 14])
print(my_list)  # [10, 9, 8, 7, 6, 11, 12, 13, 14] 


# 3. insert() 在指定位置插入元素
my_list.insert(3, 100)
print(my_list)  # [10, 9, 8, 100, 7, 6, 11, 12, 13, 14] 


# 4. remove() 删除指定元素
my_list.remove(100)
print(my_list)  # [10, 9, 8, 7, 6, 11, 12, 13, 14] 


# 5. pop() 删除指定位置的元素，并返回该元素的值
pop_value = my_list.pop(3)
print(pop_value)  # 7
print(my_list)  #   [10, 9, 7, 6, 11, 12, 13, 14] 


# 6. index() 返回指定元素的索引
index = my_list.index(12)
print(index)  # 3


# 7. count() 返回指定元素在列表中出现的次数
count = my_list.count(12)
print(count)  #  1


# 8. sort() 对列表进行排序
my_list.sort()
print(my_list)  # [5, 6, 7, 8, 9, 10, 11, 12, 13, 14] 


# 9. reverse() 反转列表
my_list.reverse()
print(my_list)  #  [14, 13, 12, 11, 10, 9, 7, 6, 5] 


# 10. copy() 复制列表
my_list_copy = my_list.copy()
print(my_list_copy)  #  [14, 13, 12, 11, 10, 9, 7, 6, 5] 


# 11 clear() 清空列表
my_list.clear()
print(my_list)  # []
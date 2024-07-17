# set 函数
# 创建集合
my_set = {1, 2, 3, 4, 5}

# 1. add() 为集合添加元素
my_set.add(6)
print("添加元素后的集合:", my_set)  # 输出: 添加元素后的集合: {1, 2, 3, 4, 5, 6}

# 2. clear() 移除集合中的所有元素
my_set.clear()
print("清空后的集合:", my_set)  # 输出: 清空后的集合: set()

# 3. copy() 拷贝一个集合
my_set = {1, 2, 3, 4, 5}
copied_set = my_set.copy()
print("拷贝的集合:", copied_set)  # 输出: 拷贝的集合: {1, 2, 3, 4, 5}

# 4. difference() 返回多个集合的差集
another_set = {4, 5, 6}
diff_set = my_set.difference(another_set)
print("差集:", diff_set)  # 输出: 差集: {1, 2, 3}

# 5. difference_update() 移除集合中的元素，该元素在指定的集合也存在
my_set.difference_update(another_set)
print("更新差集后的集合:", my_set)  # 输出: 更新差集后的集合: {1, 2, 3}

# 6. discard() 删除集合中指定的元素
my_set.discard(3)
print("删除元素后的集合:", my_set)  # 输出: 删除元素后的集合: {1, 2}

# 7. intersection() 返回集合的交集
my_set = {1, 2, 3, 4, 5}
intersection_set = my_set.intersection(another_set)
print("交集:", intersection_set)  # 输出: 交集: {4, 5}

# 8. intersection_update() 返回集合的交集，并更新原始集合
my_set.intersection_update(another_set)
print("更新交集后的集合:", my_set)  # 输出: 更新交集后的集合: {4, 5}

# 9. isdisjoint() 判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False
new_set = {7, 8, 9}
print("my_set 和 new_set 是否无交集:", my_set.isdisjoint(new_set))  # 输出: my_set 和 new_set 是否无交集: True

# 10. issubset() 判断指定集合是否为该方法参数集合的子集
subset = {4}
print("subset 是否是 my_set 的子集:", subset.issubset(my_set))  # 输出: subset 是否是 my_set 的子集: True

# 11. issuperset() 判断该方法的参数集合是否为指定集合的子集
print("my_set 是否是 subset 的超集:", my_set.issuperset(subset))  # 输出: my_set 是否是 subset 的超集: True

# 12. pop() 随机移除元素
popped_element = my_set.pop()
print("随机移除的元素:", popped_element)  # 输出: 随机移除的元素: 4
print("移除元素后的集合:", my_set)  # 输出: 移除元素后的集合: {5}

# 13. remove() 移除指定元素
my_set.remove(5)
print("移除指定元素后的集合:", my_set)  # 输出: 移除指定元素后的集合: set()

# 14. symmetric_difference() 返回两个集合中不重复的元素集合
symmetric_diff_set = my_set.symmetric_difference(another_set)
print("对称差集:", symmetric_diff_set)  # 输出:  对称差集: {1, 2, 3, 6}

# 15. symmetric_difference_update() 移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中
my_set.symmetric_difference_update(another_set)
print("更新对称差集后的集合:", my_set)  # 输出: 更新对称差集后的集合: {1, 2, 3, 6}

# 16. union() 返回两个集合的并集
union_set = my_set.union(new_set)
print("并集:", union_set)  # 输出: 并集: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# 17. update() 给集合添加元素
my_set.update([10, 11])
print("更新添加元素后的集合:", my_set)  # 输出: 更新添加元素后的集合: {1, 2, 3, 6, 10, 11}

# 18. len() 计算集合元素个数
print("集合元素个数:", len(my_set))  # 输出: 集合元素个数: 6
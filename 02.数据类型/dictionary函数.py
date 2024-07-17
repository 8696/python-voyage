# 字典函数

# 1. dict.clear()
# 清空字典中的所有元素
my_dict = {'a': 1, 'b': 2}
print("原始字典：", my_dict)  # {'a': 1, 'b': 2}
my_dict.clear()
print("清空后的字典：", my_dict)  # {}

# 2. dict.copy()
# 返回字典的浅复制
original_dict = {'a': 1, 'b': 2}
copied_dict = original_dict.copy()
print("原始字典：", original_dict)  # {'a': 1, 'b': 2}
print("复制后的字典：", copied_dict)  # {'a': 1, 'b': 2}

# 3. dict.fromkeys()
# 创建一个新字典，以序列中的元素作为字典的键，值为统一的默认值
keys = ['a', 'b', 'c']
new_dict = dict.fromkeys(keys, 0)
print("创建的新字典：", new_dict)    # {'a': 0, 'b': 0, 'c': 0}

# 4. dict.get(key, default=None)
# 返回指定键的值，如果键不存在则返回默认值
my_dict = {'a': 1, 'b': 2}
print("获取存在的键 'a' 的值：", my_dict.get('a'))  # 1
print("获取不存在的键 'c' 的值（默认）：", my_dict.get('c'))  # None
print("获取不存在的键 'c' 的值（自定义默认）：", my_dict.get('c', '自定义默认值'))  # 自定义默认值

# 5. key in dict
# 检查键是否存在于字典中
my_dict = {'a': 1, 'b': 2}
print("'a' 是否在字典中：", 'a' in my_dict)  # True
print("'c' 是否在字典中：", 'c' in my_dict)      # False

# 6. dict.items()
# 返回字典的键值对视图
my_dict = {'a': 1, 'b': 2}
print("字典的键值对视图：", my_dict.items())  # dict_items([('a', 1), ('b', 2)])

# 7. dict.keys()
# 返回字典的键视图
my_dict = {'a': 1, 'b': 2}
print("字典的键视图：", my_dict.keys())  # dict_keys(['a', 'b'])

# 8. dict.setdefault(key, default=None)
# 如果键存在，返回其值；如果键不存在，插入键并设置默认值
my_dict = {'a': 1, 'b': 2}
print("使用 setdefault 获取存在的键 'a' 的值：", my_dict.setdefault('a'))   # 1
print("使用 setdefault 获取不存在的键 'c' 的值（默认）：", my_dict.setdefault('c', 3))       # 3
print("字典更新为：", my_dict)  # {'a': 1, 'b': 2, 'c': 3}

# 9. dict.update(dict2)
# 使用另一个字典更新当前字典
my_dict = {'a': 1, 'b': 2}
new_dict = {'c': 3, 'd': 4}
my_dict.update(new_dict)
print("更新后的字典：", my_dict)    # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 10. dict.values()
# 返回字典的值视图
my_dict = {'a': 1, 'b': 2}
print("字典的值视图：", my_dict.values())   # dict_values([1, 2])

# 11. pop(key[,default])
# 删除并返回指定键的值，如果键不存在则返回默认值
my_dict = {'a': 1, 'b': 2}
print("删除并返回键 'a' 的值：", my_dict.pop('a'))  # 1
print("字典更新为：", my_dict)  # {'b': 2}
print("删除不存在的键 'c' 的值（默认）：", my_dict.pop('c', '不存在的键'))  # 不存在的键
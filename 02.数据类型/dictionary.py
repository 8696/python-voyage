import json
# Dictionary 字典

# 字典是一种无序的键值对集合，其中每个键值对用冒号分隔，键和值用逗号分隔。

# 创建字典
dict1 = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}

# 访问字典元素
print(dict1['name'])  # Output: Alice

# 修改字典元素
dict1['age'] = 26
print(dict1['age'])  # Output: 26


# 字典的键必须是不可变的，所以可以用数字、字符串或元组作为键，而不能用列表或字典。
dict2 = {(1, 2): 'value1', (3, 4): 'value2'}
print(dict2[(1, 2)])  # Output: value1

# 字典的键可以是数字，字符串或元组，而值可以是任意类型。
dict3 = {1: 'value1', 2: 'value2'}
print(dict3[1])  # Output: value1

# 字典的键不能重复，如果重复，后面的值会覆盖前面的值。
dict4 = {'name': 'Alice', 'age': 25, 'name': 'Bob'}
print(dict4['name'])  # Output: Bob

# 字典的键值对可以动态添加、删除。
dict5 = {'name': 'Alice', 'age': 25}
dict5['city'] = 'Beijing'
del dict5['age']
print(dict5)  # Output: {'name': 'Alice', 'city': 'Beijing'}  

# 字典的键值对可以遍历。  
dict6 = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}
for key, value in dict6.items():
    print(key, value)  # Output: name Alice, age 25, city Beijing 

# 字典的键值对可以排序。  
dict7 = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}
sorted_dict = dict(sorted(dict7.items()))
print(sorted_dict)  # Output: {'age': 25, 'city': 'Beijing', 'name': 'Alice'} 


# 字典的键值对可以合并。  
dict8 = {'name': 'Alice', 'age': 25}
dict9 = {'city': 'Beijing'}
dict8.update(dict9)
print(dict8)  # Output: {'name': 'Alice', 'age': 25, 'city': 'Beijing'}     


# 字典的键值对可以复制。  
dict10 = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}
dict11 = dict10.copy()
print(dict11)  # Output: {'name': 'Alice', 'age': 25, 'city': 'Beijing'}      

# 字典的键值对可以序列化。  
dict12 = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}
json_str = json.dumps(dict12)
print(json_str)  # Output: {"name": "Alice", "age": 25, "city": "Beijing"}    

# 字典的键值对可以从文件中读取。  
dict13 = json.loads('{"name": "Alice", "age": 25, "city": "Beijing"}')
print(dict13)  # Output: {'name': 'Alice', 'age': 25, 'city': 'Beijing'}      

# 字典的键值对可以导出为JSON格式。  
dict14 = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}
json_str = json.dumps(dict14, indent=4)
print(json_str)  # Output: {"name": "Alice",    "age": 25,    "city": "Beijing"}
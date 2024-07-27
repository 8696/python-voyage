import re

# 匹配所有数字
result = re.findall(r'\d+', '123 456 789 0')
print(result)  # ['123', '456', '789', '0'] 


result = re.findall(r'\d', '123 456 789 0')
print(result)  # ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


# 匹配所有字母
result = re.findall(r'\w+', 'Hello-World!')
print(result)  # ['Hello', 'World'] 


# 匹配所有字母和数字
result = re.findall(r'\w+', 'Hello-World! 123')
print(result)  # ['Hello', 'World', '123'] 


# 匹配所有字母和数字，并限制长度为3
result = re.findall(r'\w{3}', 'Hello-World! 123')
print(result)  # ['Hel', 'Wor', '123'] 


# 匹配所有以数字开头的单词
result = re.findall(r'\d\w+', '123 Hello 456 World 789')
print(result)  # ['123', '456', '789']



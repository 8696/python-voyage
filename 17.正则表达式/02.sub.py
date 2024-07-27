import re

# 使用 sub() 方法替换字符串中的匹配项
text = "My phone number is 123-456-7890."
result = re.sub(r'\d', '#', text)
print(result)  # 输出：My phone number is ###-###-####.

#  只匹配3次
result = re.sub(r'\d', '#', '1111111', 3) 
print(result)  # 输出：###1111111 



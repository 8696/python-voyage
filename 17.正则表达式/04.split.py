# split

import re

text = "The rain in Spain falls mainly in the plain."
pattern = r'\s+'  # 以空白字符分割
parts = re.split(pattern, text)
print(parts)  # 输出 ['The', 'rain', 'in', 'Spain', 'falls', 'mainly', 'in', 'the', 'plain.']


text = "one,two,three,four"
pattern = r","
result = re.split(pattern, text)
print(result)  # 输出 ['one', 'two', 'three', 'four']



text = "a b c d e"
pattern = r"\w+"
result = re.split(pattern, text)
print(result)  # 输出['', ' ', ' ', ' ', ' ', '']




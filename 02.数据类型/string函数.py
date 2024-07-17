string = "Hello, World!"

# 1. capitalize()：将字符串的首字母大写
print(string.capitalize())    # Output: Hello, World!

# 2. center(width, fillchar)：返回一个指定宽度居中的字符串，fillchar 为填充字符（默认为空格）
print(string.center(30, '*'))   # Output: **********Hello, World!

# 3. count(str, beg= 0,end=len(string))：返回 str 在字符串中出现的次数，可指定范围
print(string.count('l'))   # Output: 3
print(string.count('l', 7, 12))   # Output: 1

# 4. bytes.decode(encoding="utf-8", errors="strict")：Python3 中，用于解码字节对象
# 示例：假设我们有一个编码后的字节对象
encoded_bytes = string.encode('utf-8')
print(encoded_bytes.decode('utf-8'))   # 解码为 UTF-8

# 5. encode(encoding='UTF-8',errors='strict')：以指定编码格式编码字符串
encoded_string = string.encode('utf-8')
print(encoded_string)   # Output: b'Hello, World!'

# 6. endswith(suffix, beg=0, end=len(string))：检查字符串是否以指定后缀结束，可指定范围
print(string.endswith('!'))   # Output: True
print(string.endswith('World', 7))   # Output: True

# 7. expandtabs(tabsize=8)：将字符串中的制表符转换为指定数量的空格
string_with_tabs = "Hello\tWorld"
print(string_with_tabs.expandtabs())   # Output: Hello    World

# 8. find(str, beg=0, end=len(string))：查找字符串中是否包含指定子串，返回首次出现的索引，可指定范围，未找到返回 -1
print(string.find('World'))   # Output: 7
print(string.find('Python'))   # Output: -1

# 9. index(str, beg=0, end=len(string))：与 find 类似，未找到时抛出异常
print(string.index('World'))   # Output: 7
# 以下代码会抛出异常
# print(string.index('Python'))  

# 10. isalnum()：检查字符串是否由字母和数字组成
print(string.isalnum())    # Output: True

# 11. isalpha()：检查字符串是否只包含字母
print(string.isalpha())   # Output: True

# 12. isdigit()：检查字符串是否只包含数字
num_string = "123"
print(num_string.isdigit())   # Output: True

# 13. islower()：检查字符串是否全为小写
print(string.islower())   # Output: True

# 14. isnumeric()：检查字符串是否只包含数字字符
num_string2 = "12345"
print(num_string2.isnumeric())   # Output: True

# 15. isspace()：检查字符串是否只包含空白字符
space_string = "   "
print(space_string.isspace())   # Output: True

# 16. istitle()：检查字符串是否符合标题格式（每个单词首字母大写）
title_string = "Hello World"
print(title_string.istitle())   # Output: True

# 17. isupper()：检查字符串是否全为大写
print(string.isupper())   # Output: False

# 18. join(seq)：以指定字符串连接序列中的元素
seq = ["Hello", "World"]
print(",".join(seq))   #   Output: Hello,World

# 19. len(string)：返回字符串的长度
print(len(string))   # Output: 13

# 20. ljust(width[, fillchar])：返回左对齐并填充指定字符至指定宽度的字符串
print(string.ljust(30, '*'))   # Output: Hello, World!**********

# 21. lower()：将字符串转换为小写
print(string.lower())   # Output: hello, world!

# 22. lstrip()：截掉字符串左边的空格或指定字符
string2 = "   Hello"
print(string2.lstrip())   # Output: Hello

# 23. maketrans()：创建字符映射的转换表
# 示例：创建一个转换表，将 'a' 转换为 'A'，'b' 转换为 'B'
trans_table = str.maketrans('ab', 'AB')
print("abc".translate(trans_table))   # Output: Abc

# 24. max(str)：返回字符串中最大的字符
print(max(string))   # Output: 'z'

# 25. min(str)：返回字符串中最小的字符
print(min(string))   # Output: '!'

# 26. replace(old, new [, max])：替换字符串中的子串，可指定替换次数
print(string.replace('World', 'Python'))   # Output: Hello, Python!
print(string.replace('l', 'L', 2))   #   Output: HeLLo, World!

# 27. rfind(str, beg=0,end=len(string))：从右往左查找子串的索引
print(string.rfind('o'))   # Output: 7

# 28. rindex( str, beg=0, end=len(string))：与 rfind 类似，未找到时抛出异常
print(string.rindex('o'))   # Output: 7

# 29. rjust(width,[, fillchar])：返回右对齐并填充指定字符至指定宽度的字符串
print(string.rjust(30, '*'))   # Output: **********Hello, World!

# 30. rstrip()：截掉字符串右边的空格或指定字符
string3 = "Hello   "
print(string3.rstrip())  # Output: Hello

# 31. split(str="", num=string.count(str))：按指定分隔符分割字符串，可指定分割次数
print(string.split(','))   #   Output: ['Hello', 'World!']
print(string.split(' ', 1))  #  Output: ['Hello,', 'World!']

# 32. splitlines([keepends])：按行分割字符串，可选择是否保留换行符
multiline_string = "Hello\nWorld"
print(multiline_string.splitlines())  # Output: ['Hello', 'World']
print(multiline_string.splitlines(True))  # Output: ['Hello\n', 'World']

# 33. startswith(substr, beg=0,end=len(string))：检查字符串是否以指定子串开头，可指定范围
print(string.startswith('Hello'))  # Output: True
print(string.startswith('World', 7))  # Output: True

# 34. strip([chars])：截掉字符串两边的空格或指定字符
string4 = "  Hello  "
print(string4.strip())  # Output: Hello

# 35. swapcase()：转换字符串的大小写
print(string.swapcase())  # Output: HELLO, WORLD!

# 36. title()：将字符串转换为标题格式
print(string.title())  # Output: Hello, World!

# 37. translate(table, deletechars="")：根据转换表转换字符，可指定要删除的字符
# 示例：创建一个转换表，将 'o' 转换为 '0'
trans_table2 = str.maketrans('o', '0')
print(string.translate(trans_table2))  # Output: Hell0 W0rld!

# 38. upper()：将字符串转换为大写
print(string.upper())  # Output: HELLO, WORLD!

# 39. zfill (width)：在字符串左边填充 0 至指定宽度
num_string3 = "12"
print(num_string3.zfill(5))  # Output: 00012

# 40. isdecimal()：检查字符串是否只包含十进制数字
decimal_string = "123"
print(decimal_string.isdecimal())  # Output: True
# String 字符串 
# 字符串是由零个或多个字符组成的序列，每个字符都用一个 ASCII 码表示。
# Python 中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符。

# 创建字符串
string1 = "Hello, world!"  # 使用双引号创建字符串
string2 = 'Hello, world!'  # 使用单引号创建字符串
string3 = "I'm a string."   # 创建包含单引号的字符串
string4 = 'I\'m a string.'   # 使用反斜杠转义单引号
string5 = "This is a \n new line."   # 使用反斜杠转义换行符

# 访问字符串中的字符
print(string1[0])   # 访问第一个字符
print(string1[6])   # 访问第七个字符
print(string1[-1])  # 访问倒数第一个字符

# 字符串的运算
string6 = "Hello, " + "world!"   # 字符串连接
print(string6)   # 输出连接后的字符串

string7 = "Hello, " * 3   # 字符串重复
print(string7)   # 输出重复后的字符串

# 字符串的长度
print(len(string1))   # 输出字符串长度

# 字符串的格式化
string8 = "My name is {} and I'm {} years old.".format("Alice", 25)  # 格式化字符串
print(string8)   # 输出格式化后的字符串

# 字符串的切片
string9 = "Hello, world!"
print(string9[0:5])   # 输出索引0到4的子字符串
print(string9[6:11])  # 输出索引6到10的子字符串
print(string9[6:])    # 输出从索引6开始到字符串末尾的子字符串
print(string9[:5])    # 输出从开始到索引5的子字符串
print(string9[::2])   # 每隔一个字符输出整个字符串

# 字符串的比较
string10 = "Hello, world!"
string11 = "Hello, world!"
string12 = "Hello, Python!"

# 输出字符串的比较结果
print(string10 == string11)
print(string10 == string12)
print(string10 < string12)
print(string10 > string12)
print(string10 <= string12)
print(string10 >= string12)

# 字符串的成员资格
string13 = "Hello, world!"
print("H" in string13)   # 判断字符 "H" 是否在字符串中
print("h" in string13)   # 判断字符 "h" 是否在字符串中
print("world" not in string13)   # 判断子字符串 "world" 是否不在字符串中
print("Python" not in string13)   # 判断子字符串 "Python" 是否不在字符串中

# 字符串的转换
string14 = "123"  
print(int(string14))   # 转换为整数
print(float(string14))   # 转换为浮点数
print(str(123))   # 转换为字符串
print(bool("Hello, world!"))   # 转换为布尔值
print(bool(""))   # 转换为空字符串时的布尔值

# 字符串的编码
string15 = "Hello, world!"
print(string15.encode())   # 编码字符串为字节类型
print(string15.encode("utf-8"))   # 使用 utf-8 编码字符串
print(string15.encode("ascii"))   # 使用 ascii 编码字符串

# 字符串的解码
string16 = b'Hello, world!'
print(string16.decode())   # 解码字节类型为字符串
print(string16.decode("utf-8"))   # 使用 utf-8 解码字节类型为字符串
print(string16.decode("ascii"))   # 使用 ascii 解码字节类型为字符串

# 字符串的格式化
string17 = "My name is {} and I'm {} years old."
print(string17.format("Alice", 25))   # 格式化字符串

# 字符串的格式化符号
string18 = "My name is {name} and I'm {age} years old."
print(string18.format(name="Alice", age=25))   # 使用命名方式格式化字符串

# 字符串的格式化符号的位置
string19 = "My name is {1} and I'm {0} years old."
print(string19.format(25, "Alice"))   # 根据位置格式化字符串

# 字符串的格式化符号的命名
string20 = "My name is {name} and I'm {age} years old."
print(string20.format(name="Alice", age=25))   # 使用命名方式格式化字符串
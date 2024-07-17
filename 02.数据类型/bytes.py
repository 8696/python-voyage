# Bytes 类型

# 字节串（Bytes）是二进制数据序列，通常用于存储文本或二进制数据。

# 创建字节串
b = b'hello, world'
print(b)  # b'hello, world'

# 字节串的索引和切片
print(b[0])  # 104
print(b[1:4])  # b'ell'


# 字节串的操作
# 字节串的操作与字符串类似，但字节串只能包含字节值。

# 编码和解码
# 字节串可以编码为字符串，也可以解码为字节串。

# 编码
s = 'hello, world'
b = s.encode('utf-8')
print(b)  # b'hello, world'

# 解码
b = b'hello, world'
s = b.decode('utf-8')
print(s)  # hello, world  

# 字节串的其他操作
# 查找
# 字节串可以使用 find() 方法查找子串的位置。

b = b'hello, world'
print(b.find(b'l'))  # 2
print(b.find(b'z'))  # -1 


# 连接
# 字节串可以使用 join() 方法连接。

b1 = b'hello'
b2 = b'world'
b3 = b1 + b2
print(b3)  # b'helloworld'

b4 = b', '
b5 = b1 + b4 + b2
print(b5)  # b'hello, world'


# 字节串的其他方法
# isalnum() 方法：判断字节串是否只包含字母和数字。

b = b'hello123'
print(b.isalnum())  # True

b = b'hello world'
print(b.isalnum())  # False 

# isalpha() 方法：判断字节串是否只包含字母。

b = b'hello'
print(b.isalpha())  # True

b = b'hello world'
print(b.isalpha())  # False 

# isascii() 方法：判断字节串是否只包含 ASCII 字符。

b = b'hello, world'
print(b.isascii())  # True

b = b'\x80'
print(b.isascii())  # False 


# isdigit() 方法：判断字节串是否只包含数字。

b = b'123'
print(b.isdigit())  # True

b = b'hello123'
print(b.isdigit())  # False 

# islower() 方法：判断字节串是否只包含小写字母。

b = b'hello'
print(b.islower())  # True

b = b'HELLO'
print(b.islower())  # False 
# isupper() 方法：判断字节串是否只包含大写字母。

b = b'WORLD'
print(b.isupper())  # True

b = b'world'
print(b.isupper())  # False 

# isspace() 方法：判断字节串是否只包含空白字符。

b = b' '
print(b.isspace())  # True

b = b'hello'
print(b.isspace())  # False 


# lower() 方法：转换字节串为小写。

b = b'HELLO'
print(b.lower())  # b'hello'  

# upper() 方法：转换字节串为大写。

b = b'world'
print(b.upper())  # b'WORLD'

# replace() 方法：替换字节串中的子串。

b = b'hello, world'
print(b.replace(b'l', b'z'))  # b'hezzo, worzd'


# split() 方法：分割字节串。

b = b'hello, world'
print(b.split(b','))  # [b'hello', b' world']

# strip() 方法：去除字节串两端的空白字符。  

b = b'  hello, world  '
print(b.strip())  # b'hello, world'


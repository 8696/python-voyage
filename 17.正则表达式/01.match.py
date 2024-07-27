# 正则表达式匹配
import re

# 匹配字符串
string = 'helloworld'

# 检查字符串是否是纯字母
match = re.compile(r'^[a-zA-Z]+$').match(string)
print(match)
# 输出匹配结果
if match:
    print('1匹配成功')
else:
    print('1匹配失败')

# 检查字符串是否是纯数字
match = re.compile(r'^[0-9]+$').match('1234567890')
print(match)
# 输出匹配结果
if match:
    print('2匹配成功')
else:
    print('2匹配失败')


# 检查是否是合法的电话号码
match = re.compile(r'^(13\d|14[57]|15\d|17\d|18\d)\d{8}$').match('13012345678')
print(match)
# 输出匹配结果
if match:
    print('3匹配成功')
else:
    print('3匹配失败')


# 检查是否是合法的邮箱地址
match = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$').match('123@123.com')
print(match)
# 输出匹配结果
if match:
    print('4匹配成功')
else:
    print('4匹配失败')

# 检查字符串里面是否出现了 hello
match = re.compile(r'hello').match('2hello world')
print(match) # 输出 None
match = re.compile(r'hello').search('2hello world')
print(match) # 输出 <re.Match object; span=(2, 6), match='hello'>

# 输出匹配结果
if match:
    print('5匹配成功')
else:
    print('5匹配失败')


# match 和 search 的区别
# match 只匹配字符串的开始位置，如果字符串的开始位置不匹配，则匹配失败；
# search 匹配整个字符串，如果字符串中有多个匹配项，只返回第一个匹配项。
 
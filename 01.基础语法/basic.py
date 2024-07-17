# -*- coding: utf-8 -*-
print ('hello, world!')

# 标识符
# 第一个字符必须是字母表中字母或下划线 _ 
# 标识符的其他的部分由字母、数字和下划线组成
# 标识符对大小写敏感

#### python保留字
import keyword
print(keyword.kwlist)

 
### 注释

#第一个注释
#第二个注释
 
'''
第三注释
第四注释
'''
 
"""
第五注释
第六注释
"""
print ("Hello, Python!")


### 行与缩进
# python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。
# 缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。实例如下：
if True:
  print ("True")
else:
    print ("False")



### 多行语句
# Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠 \ 来实现多行语句，例如：
total = 'item_one-' + \
        'item_two-' + \
        'item_three'
print (total)

#在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 \，例如：
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
print (total)







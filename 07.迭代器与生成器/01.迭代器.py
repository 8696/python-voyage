# 迭代是 Python 最强大的功能之一，是访问集合元素的一种方式。

# 迭代器是一个可以记住遍历的位置的对象。

# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

# 迭代器有两个基本的方法：iter() 和 next()

# 字符串，列表或元组对象都可用于创建迭代器

# 字符串
s = "hel"
it = iter(s)
print(next(it))  # h
print(next(it))  # e
print(next(it))  # l


# 列表
lst = [1, 2, 3]
it = iter(lst)
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3


# 元组
tpl = (4, 5, 6)
it = iter(tpl)
print(next(it))  # 4
print(next(it))  # 5
print(next(it))  # 6


# 迭代器对象可以使用常规for语句进行遍历
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x)    # 输出迭代器的元素




#在 Python 中，使用了 yield 的函数被称为生成器（generator）。

# yield 是一个关键字，用于定义生成器函数，生成器函数是一种特殊的函数，可以在迭代过程中逐步产生值，而不是一次性返回所有结果。

# 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。

# 当在生成器函数中使用 yield 语句时，函数的执行将会暂停，并将 yield 后面的表达式作为当前迭代的值返回。

# 然后，每次调用生成器的 next() 方法或使用 for 循环进行迭代时，函数会从上次暂停的地方继续执行，直到再次遇到 yield 语句。这样，生成器函数可以逐步产生值，而不需要一次性计算并返回所有结果

# 举个例子

def my_generator():
    for i in range(10):
        yield i

# 调用生成器函数
gen = my_generator()


# 迭代生成器
for i in gen:
    print(i) # 0 1 2 3 4 5 6 7 8 9



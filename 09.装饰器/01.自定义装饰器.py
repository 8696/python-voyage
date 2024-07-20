# 装饰器（decorators）是 Python 中的一种高级功能，它允许你动态地修改函数或类的行为。

# 装饰器是一种函数，它接受一个函数作为参数，并返回一个新的函数或修改原来的函数。

# 装饰器的语法使用 @decorator_name 来应用在函数或方法上。

# Python 还提供了一些内置的装饰器，比如 @staticmethod 和 @classmethod，用于定义静态方法和类方法。

# 装饰器的应用场景：

# 日志记录: 装饰器可用于记录函数的调用信息、参数和返回值。
# 性能分析: 可以使用装饰器来测量函数的执行时间。
# 权限控制: 装饰器可用于限制对某些函数的访问权限。
# 缓存: 装饰器可用于实现函数结果的缓存，以提高性能。


# 基本使用
def my_decorator(func):
    # 定义装饰器函数，接受一个函数作为参数
    def wrapper(*args, **kwargs):
        print('my_decorator: ', args, kwargs)
        # 定义包装函数，接受任意参数
        print("Before calling the function")
        result = func(*args, **kwargs)
        print("After calling the function")
        print(result)
        return result
    return wrapper

@my_decorator
def my_function(x, y, **kwargs):
    print('调用my_function')
    print('my_function: ', kwargs)
    # 定义一个简单的函数，返回两个参数的和
    return x * y

print(my_function(2, 3, a=4, b=5))  # Output: Before calling the function 5 After calling the function


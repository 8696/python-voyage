# 带参数的装饰器


def my_decorator(arg1, arg2):
    # 定义装饰器函数，接受两个参数
    def decorator(func):
        # 定义包装函数，接受一个函数作为参数
        def wrapper(*args, **kwargs):
            print('my_decorator: ', arg1, arg2)
            # 定义包装函数，接受任意参数
            print("Before calling the function")
            # 调用原始函数
            # 把装饰器参数传递给原始函数
            kwargs['arg1'] = arg1
            kwargs['arg2'] = arg2
            result = func(*args, **kwargs)
            print("After calling the function")
            print(result)
            return result
        return wrapper
    return decorator


@my_decorator('hello', 'world')
def my_function(x, y, **kwargs):
  
    print('调用my_function')
    print('my_function: ', kwargs)
    # 定义一个简单的函数，返回两个参数的和
    return x * y

print(my_function(2, 3, a=4, b=5))  # Output: Before calling the function 5 After calling the function
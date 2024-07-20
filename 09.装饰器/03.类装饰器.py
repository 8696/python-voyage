# 类装饰器

class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Before calling the function")
        result = self.func(*args, **kwargs)
        print("After calling the function")
        return result

@MyDecorator
def my_function(x, y):
    return x * y

print(my_function(2, 3)) # Output: Before calling the function 5 After calling the function


# 命名空间


# 全局变量
global_variable = 10  # 这是一个全局变量，处于全局命名空间

def my_function():
    print(global_variable)  # 在函数内部可以访问全局变量

my_function()


# 局部变量
def my_function():
    local_variable = 20  # 这是一个局部变量，处于当前函数的局部命名空间
    print(local_variable)

my_function()  # 可以正常打印
# 尝试在函数外部访问局部变量会报错
# print(local_variable)  # 会引发 NameError



# 命名空间的作用域
global_variable = 5  # 全局变量

def my_function():
    global_variable = 15  # 这里创建了一个同名的局部变量，而不是修改全局变量
    print(global_variable)  # 打印的是局部变量的值

my_function()
print(global_variable)  # 5
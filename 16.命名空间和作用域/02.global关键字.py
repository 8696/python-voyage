# 全局变量
a = 10

def func():
    global a
    a = 20
    def inner_func():
        a = 30
        print(a) # 30 因为 a 是 inner_func 内部的局部变量
    inner_func()
    print(a) # 20 

func()
print(a) # 20 因为 a 是全局变量，被 func 函数改变了
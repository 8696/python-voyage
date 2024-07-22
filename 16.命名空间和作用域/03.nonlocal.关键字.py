# nonlocal关键字 
# 当在多层嵌套函数中的某一层使用 nonlocal 声明一个变量时，它能够访问和修改该层函数之外，直到找到第一个包含这个变量的外层函数中的变量
x = 0
def outer():
    x = 10

    def inner():
        # nonlocal x
        x = 20
        print("inner:", x)  # 20
      
        def inner_inner():
            nonlocal x
            x = 30
            print("inner_inner:", x)  # 30
        
        inner_inner()
        print("inner:", x)  # 30

    inner()
    print("outer:", x)  # 10

outer()

print("global:", x)  # 0
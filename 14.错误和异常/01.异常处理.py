# 异常处理

try:
    # 可能发生异常的代码
    x = 1 / 0  # 除数为0
except ZeroDivisionError:
    print("除数不能为0")
except Exception as e:
    print("未知异常:", e)
else:
    print("没有异常发生")
finally:
    print("程序执行结束")  # 无论是否有异常发生都会执行


# 其他异常类型：
try:
    x = int("abc")
except ValueError:
    print("无效的整数")
except Exception as e:
    print("未知异常:", e)
else:
    print("没有异常发生")
finally:
    print("程序执行结束")


try:
    x = "1" + 2
except TypeError:
    print("类型错误")

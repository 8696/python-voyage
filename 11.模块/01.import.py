# import 导入模块

# 导入系统模块
import sys

print(sys.platform) # 输出当前系统平台

# 导入自定义模块
from module import test
from module.sub_module import test2


print(test.get_hello_world()) # 输出 "Hello World"

print(test2.get_now_date()) # 输出当前日期

print(__name__)
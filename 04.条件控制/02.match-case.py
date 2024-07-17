# 条件控制-match-case语句

# match-case语句是一种新的语法，它可以用来匹配值并执行相应的语句。
# 它的语法类似于switch语句，但它更加强大，可以匹配任意类型的值。


# 例子：
number = 1

match number:
    case 0:
        print("zero")
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case 4:
        print("four")
    case 5:
        print("five")
    case 6:
        print("six")
    case 7:
        print("seven")
    case 8:
        print("eight")
    case 9:
        print("nine")
    case _:
        print("输入错误，请输入一个数字") 


# 匹配多个值：  

number = 3

match number:
    case 0|1|2:    # 匹配0、1、2
        print("small number")
    case 3|4|5:    # 匹配3、4、5
        print("medium number")
    case 6|7|8|9:  # 匹配6、7、8、9
        print("large number")
    case _:         # 匹配其他值
        print("输入错误，请输入一个数字") 



# 匹配任意类型的值：

value = "hello"

match value:
    case str(x):
        print('string:'+ x)
    case int(x):
        print('integer:'+ str(x))
    case float(x):
        print('float:'+ str(x))
    case _:
        print("输入错误，请输入一个数字或字符串") 
# if 条件语句

age = 18
if age >= 18:
    print("您是成年人！")
else:
    print("您不是成年人！") 


# 嵌套
age = 16
if age >= 18:
    print("您是成年人！")
else:
    if age >= 6:
        print("您是青少年！")
    else:
        print("您是儿童！") 

# 多个条件
age = 16
if age >= 18 and age < 60:
    print("您是成年人！")
elif age >= 6 and age < 18:
    print("您是青少年！")
else:
    print("您是儿童！") 


# 多个条件的嵌套
age = 16
if age >= 18 and age < 60:
    print("您是成年人！")
elif age >= 6 and age < 18:
    if age >= 12:
        print("您是中学生！")
    else:
        print("您是小学生！")
else:
    print("您是儿童！") 


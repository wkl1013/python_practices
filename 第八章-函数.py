# 函数是带名字的代码块，用于完成某一项具体的工作。定义函数使用：
# def 函数名（）：
#      具体操作
# def greet_user():
#     print("Hello World!")
#
# greet_user()

# 向函数传递参数
# def add(a, b):
#     c = a + b
#     print(c)
#
# add(2, 3)

# 实参与形参, 形参只作用于函数内部
# def add(a, b):
#     c = a + b
#     print(c)
#
# a = 10
# print(a)
# add(2, 3)
# print(a)

# 关键字实参
# def add(a, b):
#     c = a - b
#     print(c)
#
# add(a = 2, b = 5)
# add(b = 5, a = 2)

# 定义函数参数时的，参数默认值
# def add(a, b, e = 10):
#     c = a + b - e
#     print(c)
#
# add(3, 5)


# 函数的返回值
# def add(a, b):
#     c = a + b
#     return c
#
# sum = add(10, 20)
# print(sum)


# 向函数中传递任意数量的实参
# def make_pizza(*toppings):
#     """打印顾客点的所有"""
#     print(toppings)
#     print(type(toppings))
#
# make_pizza("pepproni")
# make_pizza("mushroom", "green peppers", "extra cheese")


# 使用任意数量的关键字参数  **参数名 表示任意数量实参
# def build_profile(first, last, **user_info):
#     user_info["first_name"] = first
#     user_info["last_name"] = last
#     return user_info  # 返回字典
#
# user_profile = build_profile('albert', 'einstein', location = 'princeton', field='physics')
# print(user_profile)

def add(a, b):
    sum = a + b
    return sum

sum = add(5, 1)
print(sum)


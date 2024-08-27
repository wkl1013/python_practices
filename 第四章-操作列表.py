# 遍历列表操作
families = ['Mike', 'Linda', 'Jack', 'Rose']
for person in families:
    print(person)

i = 1
for person in families:
    print(f"第{i}个家庭成员是：{person}")
    i+=1

# 创建数值列表
for i in range(1, 5):
    print(i)

nums = list(range(1,5))
print(nums)
even_nums = list(range(2, 11, 2))
print(even_nums)

# 统计数字列表中元素大小
digits = list(range(1, 10))
digits.append(0)
print(digits)
print(max(digits), min(digits), sum(digits), sum(digits)/len(digits))

squares = [i ** 2 for i in range(1, 11)]
print(squares)


# 列表切片
families = ['Mike', 'Linda', 'Jack', 'Rose']
print(families[1:3])
print(families[1:])
print(families[:3])

# 列表的复制
# 指向同一个列表
my_foods = ['pizza', 'cake', 'drink', 'noodle']
friend_foods = my_foods
print(friend_foods)

my_foods.append('ice-cream')
print(my_foods)
print(friend_foods)

# 仅复制列表中的元素
my_foods = ['pizza', 'cake', 'drink', 'noodle']
friend_foods = my_foods[:]
my_foods.append("ice-cream")
print(my_foods)
print(friend_foods)

# 定义元组（元组与列表的区别：元组中的元素不可修改）
dim = (10, 20, 30, 40, 50)
print(type(dim))
print(dim)
for i in dim:
    print(i)
print(dim[1])
print(dim[-1])
# dim[1] = 21
# print(dim)
# dim.append(60)
# print(dim)

dim = (11, 21, 31, 41, 51)
print(dim)
dim1 = dim
print(dim1)









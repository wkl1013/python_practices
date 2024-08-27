# 一个简单的案例
cars = ['audi', 'Benz', 'Buick', 'Ford', 'Byd']
for car in cars:
    if car == 'audi' or car == 'Benz':
        print('有点小贵')
    else:
        print('价格还行')

# 注意区分大小写
my_car = 'Byd'
print(my_car == 'byd')

# 检查多个条件时，需要使用and or
age1 = 22
age2 = 28
result = age2 >= 25 and age1 >= 25
print(result)
result = age2 >= 25 or age1 >= 25
print(result)

# 使用条件语句检查特定值是否在列表中
my_fruit = ['apple', 'banana', 'orange', 'pee']
if 'orange' not in my_fruit:
    print(f'We like same fruit for orange')


# if语句中的多分支结构：if-elif-else:
age = 16
if age <= 14:
    print("He is a child.")
elif age < 18:
    print('He is a youth.')
else:
    print('He is a adult.')



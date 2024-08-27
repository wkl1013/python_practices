# 一个真是案例,字典使用{}将元素包裹起来，并通过键值对的方式进行存储。Key：Value
house = {'Car': 'Byd', 'Refrigerator': 'Hair', 'Conditioner': 'Gree'}
print(house['Car'])
print(house['Refrigerator'])

# 添加键值对
house['Color'] = 'white'
house['Floor'] = 7
print(house)

# 修改字典中的值
print(house)
house['Car'] = 'Audi'
print(house)

# 删除键值对
del house['Floor']
print(house)

# 使用get访问键值对
print(house)
floor_num = house.get('floor', 'This is no floor value in dict')
print(floor_num)
print(type(floor_num))



# 遍历字典操作 使用  字典的items()属性
house = {'Car': 'Byd', 'Refrigerator': 'Hair', 'Conditioner': 'Gree'}
for key, value in house.items():
    print(key, value)

# 遍历字典中所有的键  keys()可省略
for key in house.keys():
    print(key)

# 遍历字典中的所有值，  values()
for value in house.values():
    print(value)
print(type(house.values()))
bike = ['把手', '轮胎', '刹车', '喇叭']
print(bike)

# 访问列表元素
print(bike[1])
print(bike[-1])

# 列表的修改，添加，删除元素
motorcycle = ['发动机', '轮胎', '刹车', '喇叭', '排气管', '油箱', '电瓶']
motorcycle[-1] = '电瓶坏了'
print(motorcycle)

# 末尾插入元素
motorcycle.append("脚蹬子")
print(motorcycle)

# 指定索引位置插入元素
motorcycle.insert(1, '反光镜')
print(motorcycle)

# 删除指定索引的元素
del motorcycle[0]
print(motorcycle)

# 弹出最后位置的元素
print(motorcycle.pop())
print(motorcycle)

# 移除指定元素（有多个相同元素）
motorcycle.remove('刹车')
print(motorcycle)



# 组织列表（永久改变列表中元素顺序） list.sort()
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
cars_ = ['bmw', 'baw', 'audi', 'toyota', 'subaru']
cars_.sort()
print(cars_)

# 临时排序 sorted(list)
cars = ['bmw', 'audi', 'toyota', 'subaru']
sorted(cars)
print(cars)

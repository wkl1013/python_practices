# # 打开并读取一个TXT文件
# with open("files/pi_digits.txt") as file_object:
#     contents = file_object.read()
# print(contents)
#
# # 逐行读取文件
# with open("files/pi_digits.txt") as file_object:
#     for line in file_object:
#         print(line)
#
# with open("files/pi_digits.txt") as file_object:
#     content = file_object.readlines()
# print(content)
#
# # 写入文件内容 “w”写入模式
# with open("files/programming.txt", "w") as file_object:
#     file_object.write("I love programming.")
#
# # 附加模式，"a"，不会清空文件中之前的内容
# with open("files/programming.txt", 'a') as file_object:
#     file_object.write("\nBest language is python.")

# # 程序记录客户信息
# while True:
#     name = input("请输入您的姓名：")
#     age = input("请输入您的年龄：")
#
#     with open("files/clients.txt", 'w') as file_object:
#         file_object.write(f'name: {name}  age: {age}\n')
#     print("该条信息记录成功！")
#     answer = input("是否继续 y/n:")
#     if answer == "n":
#         file_object.close()
#         break


# 异常处理，使用  try-except代码块
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print('不能使用0作为除数！')


# 数字输入实例, 正常执行内容在 else 中编写
# num1 = input("请输入被除数：")
# num2 = input("请输入除数：")
#
# try:
#     result = int(num1) / int(num2)
# except ZeroDivisionError:
#     print('除数不能为0，请重新输入')
# else:
#     print(f'结果是：{result}')


# 文本分析
def word_count(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"{filename}这个文件不存在。")
    else:
        words = contents.split()
        num_words = len(words)
        return num_words

books = ['alice.txt', 'little_woman.txt','siddhartha.txt']
for book in books:
    num_words = word_count(f'./files/{book}')
    print(num_words)

print("===============================================================================")
# 存储数据,使用 json.dump()和 json.load()
# json.dump()存储内容为一个 json 文件
# json.load()加载 json 文件中的内容

import json

numbers = [1, 2, 3, 4, 5]
filename = 'number'
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(numbers, f)
f.close()

with open(filename, 'r', encoding='utf-8') as f:
    numbers = json.load(f)
    print(numbers)
f.close()


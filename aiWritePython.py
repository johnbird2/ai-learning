# ============================================
# Python 入门练习 - 适合刚学的同学
# 运行方式：在终端输入 python aiWritePython.py
# ============================================

print("=== 1. 打印文字 ===")
print("你好，Python！")
print("我今年", 18, "岁")  # 逗号会自动加空格


print("\n=== 2. 变量 ===")
name = "小明"
age = 18
height = 1.75
is_student = True

print("姓名:", name)
print("年龄:", age)
print("身高:", height, "米")
print("是学生吗:", is_student)


print("\n=== 3. 简单计算 ===")
a = 10
b = 3
print("加法:", a + b)   # 13
print("减法:", a - b)   # 7
print("乘法:", a * b)   # 30
print("除法:", a / b)   # 3.333...
print("整除:", a // b)  # 3（只取整数部分）
print("取余:", a % b)   # 1（余数）


print("\n=== 4. 字符串拼接 ===")
greeting = "你好，" + name + "！"
message = f"我叫{name}，今年{age}岁"  # f-string，推荐用法
print(greeting)
print(message)


print("\n=== 5. 条件判断 if / else ===")
score = 85

if score >= 90:
    print("优秀！")
elif score >= 60:
    print("及格了")
else:
    print("需要加油")


print("\n=== 6. for 循环 ===")
print("数数 1 到 5：")
for i in range(1, 6):  # 1, 2, 3, 4, 5
    print("  第", i, "次")


print("\n=== 7. 列表 list ===")
fruits = ["苹果", "香蕉", "橙子"]
print("水果列表:", fruits)
print("第一个水果:", fruits[0])   # 索引从 0 开始
print("列表长度:", len(fruits))

fruits.append("葡萄")  # 添加元素
print("添加后:", fruits)


print("\n=== 8. 函数 ===")
def say_hello(person):
    """向某人打招呼"""
    return f"你好，{person}！欢迎学习 Python。"

print(say_hello("小红"))


print("\n=== 9. 小练习：猜数字（取消下面注释来试试）===")
# import random
# secret = random.randint(1, 10)  # 随机 1~10 的整数
# guess = int(input("猜一个 1 到 10 的数字："))
# if guess == secret:
#     print("猜对了！")
# else:
#     print(f"猜错了，答案是 {secret}")

print("\n学习完成！试着改改上面的数字和文字，再运行一次看看效果吧")


#看了上面例子自己写一个试试
print("---测试学习效果---")

def helloWorld(name):
    return f"你好，{name}！欢迎学习 Python。"
print(helloWorld("小冯"))
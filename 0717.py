'''
Author: fengjian
Date: 2026-07-17 10:37:05
LastEditTime: 2026-07-20 09:14:08
LastEditors: fengjian
Description: 
FilePath: \ai-learning\0717.py
'''
# python3可以在一行使用多语句,语句之间用分号隔开
print("Hello, World!"); print("Hello, Python!")
import sys; x = 'john'; sys.stdout.write(x + '\n'+x+x)

#交互命令(需要在底部终端输入py 再去写)
# >>> import sys; x = 'john'; sys.stdout.write(x + '\n')

x=11;y=14;print("x+y的和是: ", x+y);
x=11;y=14;print("x+y的和是: " + str(x+y));
x=11;y=14;print(f"x+y的和是: {x+y}");
x='aa';y='vv';print("x+y合起来是:" + (x+y));

#print输出是换行的,如果要实现不换行需要在变量末尾加上 end=""
x="a";y="b";print(x); 
#不换行输出
print("------下面是不换行输出------")
print(x, end="")
print(y)

#import与form...import 导入
import sys
print('===========Python import mode==============')
print("命令参数为: ")
for i in sys.argv:
    print(i)
print("\n python 路径为", sys.path)

#导入特定的成员
from sys import argv,path
print('===========Python form import mode==============')
print('path', path)

#python3 Number
var1 = 1
var2 = 10
del var1 #删除单个
print(var2,'变量') #var1删除了是不能打印的,会报错
# del var1, var2 #删除多个变量

#python 支持3种数值类型(int-整型, float-浮点型, complex-复数)
print(17/3) #整整除法返回浮点型
#5.666666666666667
print(17//3) #整数除法返回向下取整后的结果
#5
print(17%3) #％操作符返回除法的余数
#2
print(5*3+2)
#17
print(5**3) #5的3次方
#125

import math
print(math.floor(2.3)) #返回数字的下舍整数
print(max(3,45,2)) #最大值
print(pow(2,3)) #2的3次方
print(min(3,45,2)) #最小值
print(round(2.3)) #四舍五入

import random
print(random.choice([1,2,3,4,5])) #随机选择列表中的一个元素
print(random.random()) #返回0到1之间的随机浮点数
print(random.randint(1,10)) #返回1到10之间的随机整数
print(random.shuffle([1,2,3,4,5])) #打乱列表中的元素顺序
print(random.uniform(1,10)) #返回1到10之间的随机浮点数
print(random.sample([1,2,3,4,5], 3)) #从列表中随机选择3个元素
print(math.e) #数学常量e
print(math.pi) #数学常量pi
print(math.sqrt(16)) #平方根
print(math.log(10)) #自然对数
print(math.log10(10)) #10的对数
print(math.log2(10)) #2的对数
print(math.sin(30)) #正弦
print(math.cos(30)) #余弦
print(math.tan(30)) #正切
print(math.asin(0.5)) #反正弦

#笔记小坑 
print("=============笔记===================")
print(round(10.5)) #10
print(round(11.5)) #12 
print(round(2.5)) #12 
print(round(3.5)) #12 

print("============================字符串学习===================================")
#python3字符串
str1 = "Hello, World!"
str2 = 'Hello, World!'
print(str1[0]) #输出H,表示字符串的第一个字符
print(str1[0:5]) #输出Hello(从0到5取值,但是第5个字符不取)
print(str1[0:5:1]) #输出Hello(从0到5取值,每隔1个字符取一个)
print(str1[0:5:3]) #输出Hl
print(str1[0:-1]) #输出Hello, World
print(str1[0:5:2]) #输出Hlo
print(str1[0::2]) #输出Hlo ol!
print(str1[0::3]) #输出Hl r!( 从 0 到末尾，每 3 个取一个（0,3,6,9,...）)

print("已更新字符串1: ", str1.replace("World", "Python"))
print("已更新字符串2: ", str1.upper()) #全部大写
print("已更新字符串3: ", str1.lower()) #全部小写
print("已更新字符串4: ", str1.title()) #首字母大写
print("已更新字符串5: ", str1.strip()) #去除字符串两端的空格
print("已更新字符串6: ", str1.split()) #以空格为分隔符，将字符串分割成列表
print("已更新字符串7: ", str1.split("o")) #以o为分隔符，将字符串分割成列表
print("已更新字符串8: ", str1.join("Python")) #将Python字符串连接成一个字符串
print("已更新字符串9: ", str1.count("o")) #统计字符串中o出现的次数
print("已更新字符串10: ", str1.find("World")) #查找字符串中World出现的位置
print("已更新字符串11: ", str1.rfind("World")) #查找字符串中World出现的最后位置
print("已更新字符串12: ", str1.capitalize()) #将字符串的第一个字符大写，其他字符小写
print("已更新字符串13: ", str1.startswith("Hello")) #检查字符串是否以Hello开头
print("已更新字符串14: ", str1.endswith("World")) #检查字符串是否以World结尾
print("已更新字符串15: ", str1.isalpha()) #检查字符串是否只包含字母
print("已更新字符串16: ", str1.isdigit()) #检查字符串是否只包含数字

print("==================字符串更新=========================")
print(str1[:8] +'Python') #更新字符串

#使用\r实现百分比进度(\r回车符,意思是吧光标移到当前行的开始位置)
import time
for i in range(101): # 添加进度条图形和百分比
    bar = '[' + '=' * (i // 2) + ' ' * (50 - i // 2) + ']'
    print(f"\r{bar} {i:3}%", end='', flush=True)
    time.sleep(0.01)
print()

#写一个字符串判断
str3="Yellows"
if ('ow' in str3):
    print("当前字符串"+str3 + "包含ow")
else:
    print("当前字符串" + str3 + "不包含ow")

#字符串格式化(%s格式化字符串, %d格式化整数, %f格式化浮点数)
print("我叫 %s,今年 %d 岁" % ("小花猫", 10))
print("我叫 %s,今年 %d 岁,身高 %.2f 米" % ("小龙", 10, 1.75))


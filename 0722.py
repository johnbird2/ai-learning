#循环for while 
#for 迭代循环,用于遍历可迭代对象
#while 循环,用于在条件为真时重复执行代码块
#break 语句用于跳出循环
#continue 语句用于跳过当前循环的剩余部分并继续下一次循环
#pass 语句用于占位符,表示什么都不做
#range() 函数用于生成一个整数序列
#enumerate() 函数用于将可迭代对象转换为枚举对象

#循环for
for i in range(5):
    print(i, end=',')
print()
for i in [1,2,3,4,5]:
    print(i, end='/')

print()
print("----------分割线-------------")
#循环while
i = 0
while i < 5:
    print(i, end='>')
    i += 1
#求1-100的和
print()
sum = 0
i = 1
while i <= 100:
    sum += i
    i += 1
print("1-100的和是:",sum)

print()
num = 2
num = int(input("请输入一个数字:"))
print("输入的数字是:",num)

#!/usr/bin/python3
 
count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")


#!/usr/bin/python3
 
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    print(site)
    if site == "Runoob":
        break

print()
for li in 'Runoob':
  print (li, end='-')

print()
#循环for中有else时,会在执行完所有循环体后执行else语句
for i in range(3):
    print(i)
else:
    print("循环结束")

#以下 for 实例中使用了 break 语句，break 语句用于跳出当前循环体，不会执行 else 子句：
#!/usr/bin/python3
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")
#打印结果
# 循环数据 Baidu
# 循环数据 Google
# 菜鸟教程!
# 完成循环!

print()
#range() 函数用于生成一个整数序列, range(start, stop, step) 表示从 start 开始到 stop 停止, step 为步长
for i in range(10):
    print(i, end=' ')
print()
for i in range(1, 10):
    print(i, end=' ')
print()
for i in range(1, 10, 2):
    print(i, end=' ')
print()
for i in range(10, 1, -1):
    print(i, end=' ')
print()
for i in range(-10, -100, -30) :
    print(i)
print()
#打印结果
# 0 1 2 3 4 5 6 7 8 9 
# 1 2 3 4 5 6 7 8 9 
# 1 3 5 7 9 
# 10 9 8 7 6 5 4 3 2 

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('循环结束。')
#打印结果(break直接打破,不再进行后续流程)
# 4 
# 3 
# 循环结束。

print()

n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('循环结束。')
#打印结果
# 4 
# 3 
# 1 
# 0 
# 循环结束。

print()
#!/usr/bin/python3
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')

#while 循环中嵌入else
print()
n = 10
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
else:
    print('循环结束。')
#打印结果
# 4 
# 3 
# 1 
# 循环结束。
print()

for char in 'PYTHON STRING':
  if char == ' ':
      break

  print(char, end='')
  
  if char == 'O':
      continue
#打印结果
# PTHYN
print()

# python3 列表
# 序列中的每个值都有对应的位置值，称之为索引，第一个索引是 0，第二个索引是 1，依此类推。
# Python 有 6 个序列的内置类型，但最常见的是列表和元组。
# 列表都可以进行的操作包括索引，切片，加，乘，检查成员。
# 此外，Python 已经内置确定序列的长度以及确定最大和最小的元素的方法。
# 列表是最常用的 Python 数据类型，它可以作为一个方括号内的逗号分隔值出现。
# 列表的数据项不需要具有相同的类型

print('=============#列表[]==================')
list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print( list[0] ) #打印结果: red
print( list[1] ) #打印结果: green
print( list[2] ) #打印结果: blue
#索引也可以从尾部开始，最后一个元素的索引为 -1，往前一位为 -2，以此类推。
print( list[-1] ) #打印结果: black
print( list[-2] ) #打印结果: white
print( list[-3] ) #打印结果: yellow
#使用下标索引来访问列表中的值，同样你也可以使用方括号 [] 的形式截取字符
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(nums[0:4]) #打印结果: [10, 20, 30, 40]
print(nums[2:]) #打印结果: [30, 40, 50, 60, 70, 80, 90] 表示从第三个元素开始到最后

list = ['Google', 'Runoob', "Zhihu", "Taobao", "Wiki"]
# 读取第二位
print ("list[1]: ", list[1]) #打印结果: Runoob
# 从第二位开始（包含）截取到倒数第二位（不包含）
print ("list[1:-2]: ", list[1:-2]) #打印结果: [Runoob, Zhihu]

#你可以对列表的数据项进行修改或更新，你也可以使用 append() 方法来添加列表项
list1 = ['Google', 'Runoob', 'Taobao']
list1.append('Baidu')
print ("更新后的列表 : ", list1) #打印结果: 更新后的列表 :  ['Google', 'Runoob', 'Taobao', 'Baidu']

#可以使用 del 语句来删除列表中的元素
list = ['Google', 'Runoob', 1997, 2000]
print ("原始列表 : ", list) #打印结果: 原始列表 :  ['Google', 'Runoob', 1997, 2000]
del list[2]
print ("删除第三个元素 : ", list) #打印结果: 删除第三个元素 :  ['Google', 'Runoob', 2000]

#列表比较需要引入 operator 模块的 eq 方法
# 导入 operator 模块
import operator
a = [1, 2]
b = [2, 3]
c = [2, 3]
print("operator.eq(a,b): ", operator.eq(a,b)) #打印结果: operator.eq(a,b):  False
print("operator.eq(c,b): ", operator.eq(c,b)) #打印结果: operator.eq(c,b):  True

# Python列表函数&方法
# len(list) 返回列表的长度
# max(list) 返回列表中最大元素
# min(list) 返回列表中最小元素
# list(seq) 将可迭代对象转换为列表
# list.append(x) 在列表末尾添加元素 x
# list.extend(seq) 在列表末尾添加序列 seq 中的元素
# list.insert(i, x) 在列表索引 i 处插入元素 x
# list.remove(x) 移除列表中第一个值为 x 的元素
# list.pop(i) 移除列表索引 i 处的元素，返回该元素
# list.index(x) 返回列表中第一个值为 x 的元素的索引
# list.count(x) 返回列表中值为 x 的元素的个数
# list.sort() 对列表进行排序
# list.reverse() 反转列表
# list.clear() 清空列表
# list.copy() 返回列表的浅拷贝
# list.pop() 移除列表末尾的元素并返回该元素

print('=============#元组()==================')
# Python 的元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号 ( )，列表使用方括号 [ ]。
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可

# 元组中只包含一个元素时，需要在元素后面添加逗号 , ，否则括号会被当作运算符使用
tup1 = (50,)
print(tup1) #打印结果: (50,)
print(tup1) #打印结果: ('Google',)
print(type(tup1)) #打印结果: <class 'tuple'>

tup2=(50)
print(tup2) #打印结果: 50
print(type(tup2)) #打印结果: <class 'int'>

# 元组可以使用下标索引来访问元组中的值
tup1 = ('Google', 'Runoob', 'Taobao', 'Wiki')
print(tup1[0]) #打印结果: Google
print(tup1[1]) #打印结果: Runoob
print(tup1[2]) #打印结果: Taobao
print(tup1[3]) #打印结果: Wiki

# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
 
# 以下修改元组元素操作是非法的。
# tup1[0] = 100 这种操作是非法的，因为元组元素是不允许修改的。

# 创建一个新的元组
tup3 = tup1 + tup2
print (tup3)

#元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
tup = ('Google', 'Runoob', 1997, 2000)
print (tup)
del tup
print ("删除后的元组 tup : ")
print (tup)


print('=============#字典{}==================')
# 字典是另一种可变容器模型，且可存储任意类型对象。
# 字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中 ,格式如下所示：
# d = {key1 : value1, key2 : value2, key3 : value3 }
# 注意：dict 作为 Python 的关键字和内置函数，变量名不建议命名为 dict

# 创建字典
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name']) #打印结果: dict['Name']:  Zara
print ("dict['Age']: ", dict['Age']) #打印结果: dict['Age']:  7

# 修改字典
dict['Age'] = 8; # 更新 Age 的值
dict['School'] = "DPS School"; # 添加新的键值对
print ("dict['Age']: ", dict['Age']) #打印结果: dict['Age']:  8
print ("dict['School']: ", dict['School']) #打印结果: dict['School']:  DPS School'

# 删除字典
del dict['Age'] # 删除 Age 键值对
print ("dict['Age']: ", dict['Age']) #打印结果: dict['Age']:  KeyError: 'Age'

#字典内置函数&方法
# len(dict) 返回字典中键值对的个数
# str(dict) 返回字典中所有的键值对，返回值是一个字符串
# type(dict) 返回字典的类型，返回值是 <class 'dict'>
# dict.keys() 返回字典中所有的键，返回值是一个列表
# dict.values() 返回字典中所有的值，返回值是一个列表
# dict.items() 返回字典中所有的键值对，返回值是一个列表
# dict.get(key) 返回指定键的值，如果键不存在返回 None
# dict.pop(key) 删除指定键的键值对，如果键不存在返回
# dict.popitem() 删除字典中最后一个键值对
# dict.clear() 清空字典
# dict.copy() 返回字典的浅拷贝
# dict.fromkeys(seq) 创建一个新的字典，其中包含 seq 中的元素作为键，所有键的值为 None
# dict.update(dict2) 将 dict2 中的键值对更新到 dict 中
# dict.setdefault(key) 如果键不存在，返回 None，如果键存在，返回

#练习
confusion = {}
confusion[1] = 1
confusion['1'] = 2
confusion[1] += 1

sum = 0
for k in confusion:
    sum += confusion[k]

print(sum) #打印结果: 4

print('=============#集合set==================')
# 集合是无序的，不重复的元素集合。
# 可以使用大括号 { } 创建集合，元素之间用逗号 , 分隔， 或者也可以使用 set() 函数创建集合。
# 集合中的元素是不允许修改的，但可以添加和删除元素。
# 集合可以使用下标索引来访问集合中的元素，但集合中的元素是无序的，所以不能使用下标索引来访问集合中的元素。
# 创建集合
set1 = {'Google', 'Runoob', 'Taobao', 'Wiki'}
print ("set1[0]: ", set1[0]) #打印结果: KeyError: 0
#类似列表推导式，同样集合支持集合推导式(Set comprehension):
set2 = {x for x in set1 if x != 'Runoob'}
print ("set2[0]: ", set2[0]) #打印结果: Wiki
print ("set2[1]: ", set2[1]) #打印结果: Google
print ("set2[2]: ", set2[2]) #打印结果: Wiki
print ("set2[3]: ", set2[3]) #打印结果: Taobao

#集合内置函数&方法
# len(set) 返回集合中元素的个数
# str(set) 返回集合中所有的元素，返回值是一个字符串
# type(set) 返回集合的类型，返回值是 <class 'set'>
# set.add(x) 在集合中添加元素 x
# set.remove(x) 删除集合中第一个值为 x 的元素
# set.discard(x) 删除集合中第一个值为 x 的元素，如果 x 不在集合中，不报错
# set.pop() 删除集合中最后一个元素并返回该元素
# set.clear() 清空集合
# set.copy() 返回集合的浅拷贝
# set.union(set2) 返回两个集合的并集
# set.intersection(set2) 返回两个集合的交集
# set.difference(set2) 返回两个集合的差集
# set.symmetric_difference(set2) 返回两个集合的对称差集
# set.issubset(set2) 判断集合是否是另一个集合的子集
#运算符
'''
算术运算符
赋值运算符
比较(关系)运算符
逻辑运算符
成员运算符
身份运算符
位运算符
预算符优先级
'''
#算术运算符
print(10+20) #30
print(10-20) #-10
print(10*20) #200 
print(10/20) #0.5 浮点数除法
print(10//20) #0 整数除法
print(10%20) #10 取余
print(10**20) #幂运算(10的20次方) 100000000000000000000
print(10**0.5) #平方根运算 3.1622776601683795
print(10**-2) #10的-2次方 0.01
print(10**-0.5) #10的-0.5次方 0.31622776601683795

#比较(关系)运算符
print("###################比较(关系)运算符####################")
print(10>20) #False
print(10<20) #True
print(10>=20) #False
print(10<=20) #True
print(10==20) #False 比较2个对象是否相等
print(10!=20) #True 不等于
# 修改变量 a 和 b 的值
a = 5
b = 20
if ( a <= b ):
   print ("5 - a 小于等于 b")
else:
   print ("5 - a 大于  b")
 
if ( b >= a ):
   print ("6 - b 大于等于 a")
else:
   print ("6 - b 小于 a")

#赋值运算符
print("###################赋值运算符#")
a = 10
b = 20
print(a) #10
print(b) #20
a += 5 #a = a + 5
print(a) #15
b -= 5 #b = b - 5
print(b) #15
a *= 2 #a = a * 2
print(a) #30
b /= 2 #b = b / 2
print(b) #7.5
a %= 2 #a = a % 2
print(a) #0
b **= 2 #b = b ** 2
print(b) #56.25
a //= 2 #a = a // 2
print(a) #0
b //= 2 #b = b // 2 取整数除法
print(b) #28.0
# 传统写法
n = 10
if n > 5:
    print(n)
# 使用海象运算符((n :=10)表示将变量n赋值为10，同时返回这个赋值结果);优点-允许在表达式内部进行赋值,可以减少代码重复,提高代码的可读性和简洁性
if (n := 10) > 5:
    print(n)

#python位运算符(按位预算符是吧数字看作二进制进行计算)
#下表中变量 a 为 60，b 为 13二进制格式如下：
print("###################位运算符#")
# a = 0011 1100
# b = 0000 1101
# a&b = 0000 1100
# a|b = 0011 1101
# a^b = 0011 0001
# ~a  = 1100 0011

#逻辑运算符
print("###################逻辑运算符#")
a = True
b = False
print(a and b) #False 且
print(a or b) #True  或
print(not a) #False
print(not b) #True

#成员运算符
print("###################成员运算符#")
a = [10,20,30,40,50]
print(10 in a) #True
print(10 not in a) #False
print(60 in a) #False
print(60 not in a) #True

#身份运算符
print("###################身份运算符#")
a = [10,20,30,40,50]
b = [10,20,30,40,50]
print(a is b) #False (is是判断两个变量是否指向同一个对象，而不是判断两个对象的内容是否相等)
print(a is not b) #True (is not是判断两个变量是否指向同一个对象，而不是判断两个对象的内容是否相等)

a = 20
b = 20
 
if ( a is b ):
   print ("1 - a 和 b 有相同的标识")
else:
   print ("1 - a 和 b 没有相同的标识")
 
if ( id(a) == id(b) ):
   print ("2 - a 和 b 有相同的标识")
else:
   print ("2 - a 和 b 没有相同的标识")
 
# 修改变量 b 的值
b = 30
if ( a is b ):
   print ("3 - a 和 b 有相同的标识")
else:
   print ("3 - a 和 b 没有相同的标识")
 
if ( a is not b ):
   print ("4 - a 和 b 没有相同的标识")
else:
   print ("4 - a 和 b 有相同的标识")

print("###################预算符优先级#")
#优先级顺序为NOT > AND > OR

xx = True
yy = False
zz = False

if not xx or yy: #等同于 (not True) or False
    print(1)
elif not xx or not yy and zz: #等同于(not True) or ((not False) and False)
    print(2)
elif not xx or yy or not yy and xx: #等同于(not True) or False or ((not False) and True)
    print(3)
else:
    print(4)

#条件控制
print("###################条件控制#")
# if 语句
a = 10
b = 20
if a > b:
    print("a 大于 b")
elif a < b:
    print("a 小于 b")
else:
    print("a 等于 b")

# for 循环
print("###################for 循环#")
for i in range(10):
    print(i)

#match 语句
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
 
print(http_error(400))
print(http_error(404))
print(http_error(418))
print(http_error(500))

#match和for in结合使用
def check_permission(status):
    match status:
        case 200:
            return "OK - 请求成功"
        case 301 | 302:
            return "Redirect - 重定向"
        case 401 | 403 | 404:
            return "Not allowed - 无权限或未找到"
        case 500 | 502 | 503:
            return "Server Error - 服务器错误"
        case _:
            return "Unknown status - 未知状态码"
 
for code in [200, 301, 403, 500, 418]:
    print(f"状态码 {code}: {check_permission(code)}")
# python3 基础语法(变量定义)
age = 20
user_name = "小冯"
_sum = 100
MAX_SIZE = 1000 # 全大写表示常量(固定不变的值)
calculate_are = 300 # 函数名(动词+名称)
StudengtInfo = "学生信息" # 类名(首字母大写-驼峰命名)
__private_var = "私有变量" # 私有变量(双下划线开头,有特殊含义)
姓名 = "小冯" # 中文变量名(不推荐使用但是合法)
var='var'
# if=221 # 关键字不能作为变量名

"""
下面是Python中的关键字:
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""

print(姓名)
print(var)

def is_valid_identifier(name):
    """
    检查变量名是否合法
    """
    try:
        exec(f"{name} = None") #None是Python中的一个特殊值,表示空值/无值
        return True
    except:
        return False

print(is_valid_identifier("姓名"))
'''合法变量名:'''
print(is_valid_identifier("var2")) # 变量名不能以数字开头
print(is_valid_identifier("int")) # 变量名不能是关键字
"""不合法变量名:"""
print(is_valid_identifier("var"))

'''条件判断(同一代码块的语句必须包含相同的缩进空格数)'''
if(True):
    print("True")
else:
    print("False")



print("----------------字符串操作----------------")
str = '1234567890'
print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第六个的字符（不包含）
print(str[2:])             # 输出从第三个开始后的所有字符
print(str[1:5:2])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)             # 输出字符串两次
print(str + '你好')         # 连接字符串
 
print('------------------------------')
 
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
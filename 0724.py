#用python3 写一个猜数字游戏

  # 猜数字游戏 - 第 1 周 Friday
  # 玩法:程序随机生成 1-100 的整数,你来猜,提示"太大"或"太小",猜中显示用了多少次

import random       # 引入 random 模块,用来生成随机数
                            
answer = random.randint(1, 100)                 # 生成 1-100 之间的随机整数作为答案
count = 0                                       # 记录猜的次数,初始为 0

print("=" * 40)
print("   欢迎来到猜数字游戏!")
print("   我已经想了一个 1-100 之间的数字")
print("=" * 40)

while True:                                     # 无限循环,直到猜中才 break
    guess_text = input("请输入你的猜测: ")      # 读取用户输入(返回字符串)
    guess = int(guess_text)                     # 转成整数

    count = count + 1                           # 次数 +1

    if guess > answer:                          # 猜大了
        print(">> 太大啦!再小一点")
    elif guess < answer:                        # 猜小了
        print(">> 太小啦!再大一点")
    else:                                       # 猜中了
        print(f">> 恭喜!答案就是 {answer},你用了 {count} 次猜中")
        break                                   # 跳出循环,游戏结束
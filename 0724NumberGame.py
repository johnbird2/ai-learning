'''
Author: fengjian
Date: 2026-07-24 16:07:33
LastEditTime: 2026-07-24 16:50:26
LastEditors: fengjian
Description: 
FilePath: \ai-learning\0724NumberGame.PY
'''
#猜数字游戏
import random

print("❤️ " * 19)
print(" " + "❤️ " * 4 + "欢迎来到猜数字游戏！" + "❤️ " * 4)
print("  " + "❤️ " * 17)
print("请选择一个难度：")
print("1. 简单（1-100，最多 10 次）")
print("2. 中等（1-100，最多 7 次）")
print("3. 困难（1-100，最多 5 次）")

difficulty = None
while difficulty not in {"1", "2", "3"}:
    difficulty = input("请输入难度编号 1/2/3：").strip()
    if difficulty not in {"1", "2", "3"}:
        print("输入无效，请输入 1、2 或 3。")

if difficulty == "1":
    max_attempts = 10
    level_name = "简单"
elif difficulty == "2":
    max_attempts = 7
    level_name = "中等"
else:
    max_attempts = 5
    level_name = "困难"

random_number = random.randint(1, 100)  # 生成一个1到100之间的随机数
print(f"你选择了 {level_name} 难度。你最多有 {max_attempts} 次猜测机会。")
print("请在心中想一个1到100之间的数字。")

count = 0
while count < max_attempts:
    print("❤️ " * 2, end=" ")
    guess_text = input("请输入你的猜测：")
    try:
        guess = int(guess_text)
    except ValueError:
        print("===== 输入无效，请输入一个整数。")
        continue

    if guess < 1 or guess > 100:
        print("===== 请输入 1 到 100 之间的数字。")
        continue

    count += 1
    if guess < random_number:
        print(f"===== 太小了，再试一次。 （已使用 {count}/{max_attempts} 次）")
    elif guess > random_number:
        print(f"===== 太大了，再试一次。 （已使用 {count}/{max_attempts} 次）")
    else:
        print(f"🌹🌹🌹🌹恭喜你，猜对了！🌹🌹🌹🌹你总共猜了 {count} 次。🌹🌹")
        break

    if count == max_attempts:
        print(f"😢 很遗憾，你已经用完所有 {max_attempts} 次机会。正确答案是 {random_number}。")

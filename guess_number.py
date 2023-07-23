# -*- coding:utf-8 -*-
"""
程序描述：编写一个叫做“猜数字”的游戏。
计算机想到一个1到20之间的随机数，让你来猜它是几。
计算机会告诉你每次猜的数太大还是太小。如果能够在6次之内猜到正确的数字，就赢得游戏。”

编写者：humidy
"""
import random


def generate_number():
    """
    :return: 返回一个1到20之间的随机数，包含1和20
    """
    computer_number = random.randint(1, 20)
    return computer_number


def guess_computer_number(computer_number):
    """
    :param computer_number: 电脑想出的数字
    :return: 返回是否猜对以及次数
    """
    # 设置给定机会的次数
    change_times = 6
    # 设定是否猜对，初始值为未猜对
    guess_right = 0
    # 初始化尝试次数
    try_times = 0
    # 警告阈值
    warm_times = 1
    # 开始竞猜
    for each_try in range(change_times):
        left_number = change_times - try_times
        # 如果竞猜次数还剩下一次，做特殊提示处理
        if left_number == warm_times:
            print("[警告]:你还剩{}次机会，要小心作答哦！".format(left_number))
        # 继续操作
        guess_number = input("[你有{}次机会]请输入你猜的数字:".format(left_number))
        if guess_number.isdigit():
            guess_number = int(guess_number)
            if guess_number > 20 or guess_number < 1:
                try_times += 1
                print("[警告]:你输入的数字不在[1-20],浪费了一次机会，还剩{}次机会".format(left_number))
                continue
        else:
            try_times += 1
            print("[警告]:你输入的不是合法数字，浪费了一次机会，还剩{}次机会，请输入整数".format(left_number))
            continue

        if guess_number > computer_number:
            try_times += 1
            print("[提示]:你猜的数字太大了")
            continue
        elif guess_number < computer_number:
            try_times += 1
            print("[提示]:你猜的数字太小了")
            continue
        else:
            try_times += 1
            guess_right = 1
            break
    return try_times, guess_right


if __name__ == "__main__":
    print("猜数游戏v1.0")
    your_name = input("[信息]:小朋友，请输入你的昵称:")
    print("[信息]:你好,{},我想出了一个1到20的整数，你来猜一猜吧。".format(your_name))
    get_num = generate_number()
    times, right = guess_computer_number(get_num)
    if right == 1:
        print("[信息]:太棒了,{}! 你猜对了我的数字{},用了{}次机会".format(your_name, get_num, times))
    else:
        print("[信息]:很遗憾，{}，你没答对! 不要泄气，总有好事会发生".format(your_name))

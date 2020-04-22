"""
for-in循环
"""
sum = 0
for x in range(101):
    sum += x
print(sum)

"""
1-100偶数求和
"""
sum = 0
for x in range(2, 101, 2):
    sum += x
print(sum)

"""
使用分支和循环一起实现偶数求和
"""
sum = 0
for x in range(1,101):
    if x % 2 == 0:
        sum += x
print(sum)

"""
猜数字游戏
"""
# import random
# answer = random.randint(1, 100)
# counter = 0
# while True:
#     counter += 1
#     number = int(input('请输入：'))
#     if number > answer:
#         print('小一点')
#     elif number < answer:
#         print('大一点')
#     else:
#         print('恭喜猜对了！')
#         break
# print('你总共猜了%d次' % counter)
# if counter > 7:
#     print('你的智商余额明显不足')
"""
循环套循环
"""
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('%d*%d=%d' % (i, j, i * j), end='\t')
#         print()

"""
练习1：输入一个正整数判断是不是素数
"""
# from math import sqrt
#
# num = int(input('请输入一个正整数：'))
# end = int(sqrt(num))
# is_prime = True
# for x in range(2, end + 1):
#     if num % x == 0:
#         is_prime = False
#         break
# if is_prime and num != 1:
#     print('%d是素数' % num)
# else:
#     print('%d不是素数' % num)

"""
练习2：输入两个正整数计算它们的最大公约数，和最小公倍数
"""
# x = int(input('x = '))
# y = int(input('y = '))
# if x > y:
#     x, y = y, x
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print('%d和%d最大公约数是%d' % (x, y, factor))
#         print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
#         break

"""
练习3：打印如下所示的三角形图案
"""
row = 5
for i in range(row):
    for k in range(i + 1):
        print('*', end='')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for h in range(row - i - 1):
        print(' ', end='')
    for h in range(2 * i + 1):
        print('*', end='')
    print()
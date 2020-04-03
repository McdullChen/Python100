"""
使用变量保存数据并进行加减乘除运算
Version:0.1
Author:Jason
a = 321
b = 12
print(a + b)
print(a - b)
print(a * b)
print(a / b)
"""

"""
使用type()检查变量的类型
a = 100
b = 12.345
c = 1 + 5j
d = 'hello,world'
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
"""

"""
使用input()函数获取键盘输入(字符串)
使用int()函数将输入的字符串转换成整数
使用print()函数输出带占位符的字符串
a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d + %d = %d' % (a, b, a * b))
print('%d - %d = %d' % (a, b, a / b))
print('%d + %d = %d' % (a, b, a // b))
print('%d - %d = %d' % (a, b, a % b))
print('%d - %d = %d' % (a, b, a ** b))
"""

"""
赋值运算符和复合赋值运算符
a = 10
b = 3
a += b
a *= a + 2
print(a)
"""

"""
比较运算符和逻辑运算符的使用
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)
print('flag0 =', flag0, 'flag1 =', flag1)
print('flag2 =', flag1, 'flag3 =', flag3)
print('flag4 =', flag4, 'flag5 =', flag5)
"""

"""
2020-04-03
练习1：华氏温度转换为摄氏温度
f = float(input('请输入华氏温度：'))
d = float(input('请输入摄氏温度：'))
c = (f - 32) / 1.8
e = (d * 1.8 + 32)
print('%.1f华氏度 = %.1f摄氏度' % (f, c), f'{d:.1f}摄氏度 = {e:.1f}华氏度')
"""


"""
练习2：输入圆的半径计算周长和面积
r = float(input('请输入圆的半径：'))
v = 2 * r * 3.14
s = r ** 2 * 3.14
print(f'圆的周长={v:.2f}', f'圆的面积={s:.2f}')
print('圆的周长：%.2f' % v, '圆的面积：%.2f' % s)
"""


"""
练习3：输入年份判断是否是闰年
"""
year = int(input('请输入年份：'))
is_leap = (year % 4 == 0 and year % 100 != 0) or \
          year % 400 == 0
print(is_leap)



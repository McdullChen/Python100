"""
用户身份验证
"""

username = input('请输入用户名：')
password = input('请输入密码：')
if username == 'admin' and password == '1':
    print('身份验证成功！')
    """
    分段函数求职
            3x - 5 (x > 1)
    f(x) =  x + 2  (-1 <= x <= 1)
            5x + 3 (x < -1)
    """

    x = float(input('x = '))
    if x > 1:
        y = 3 * x - 5
    elif x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
    print('f(%.2f) = %.2F' % (x, y))

    """
    英制单位英寸和公制单位厘米互换
    """
    value = float(input('请输入长度：'))
    unit = input('请输入单位：')
    if unit == 'in' or unit == '英寸':
        print('%f英寸 = %f厘米' % (value, value * 2.54))
    elif unit == 'cm' or unit == '厘米':
        print('%f厘米 = %f英寸' % (value, value / 2.54))
    else:
        print('请输入有效单位')
    """
    百分制成绩和等级转换
    """
    score = float(input('请输入成绩：'))
    if score > 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'E'
    print('对应的等级是：', grade)

    """
    输入三边长度如果可以构成三角形求周长和面积
    """
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    if a + b > c and a + c + b and b + c > a:
        print('周长： %f' % (a + b + c))
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - c) * (p - b)) ** 0.5
        print('面积: %f' % (area))
    else:
        print('不能构成三角形')

else:
    print('身份验证失败！')


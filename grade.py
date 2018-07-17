cj=int(input("input your number: "))
if cj >= 90:
    print("优秀")
elif cj >= 80:
    print("好")
elif cj>= 70:
    print("良")
elif cj>= 60:
    print('及格')
else:
    print("你要努力了")

score=int(input('分数: '))
if 60<=score<70:
    print('及格')
elif 70<=score<80:
    print('liang')
elif 80<=score<90:
    print('hao')
elif score>=90:
    print('youxiu')
else:
    print('你要努力了')
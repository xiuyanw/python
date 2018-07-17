import random
num=random.randint(1,10)
answer=int(input("guess a number between 1 to 10: "))
if num==answer:
    print("successful")
elif answer > num:
    print("猜大了")
else:
    print("猜小了")
print('the number is: ',num)
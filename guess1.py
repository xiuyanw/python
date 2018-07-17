import random
num = random.randint(1,10)
counter=0
while counter<5:
    guess = int(input("guess a number: "))
    if guess>num:
        print("big")
    elif guess<num:
        print("small")
    else:
        print("success")
        break
    counter+=1
else:
    print("number is:",num)

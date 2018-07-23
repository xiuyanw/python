import random

def exam():
    cmds={'+':lambda x,y:x+y,'-':lambda x,y:x-y}   #把一中的add和sub函数去掉，直接用lambda匿名函数来。
    nums=[random.randint(1,100) for i in range(2)]
    nums.sort(reverse=True)
    op = random.choice('+-')
    result=cmds[op](*nums)
    prompt="%s %s %s=" % (nums[0],op,nums[1])
    tries=0
    while tries<3:
        try:
            answer=int(input(prompt))
        except:
            continue
        if answer==result:
            print("\033[32;1mvery good\033[0m")
            break
        else:
            print("\033[31;1mWrong answer\033[0m")
            tries+=1
if __name__ == '__main__':
    while True:
        exam()
        try:
            yn=input("cotinue(y/n)?").strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt,EOFError):
            print()
            yn='n'
        if yn in 'Nn':
            break

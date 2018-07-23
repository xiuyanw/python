import random
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def exam():
    cmds={'+':add,'-':sub}
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
    else:
        print('%s %s' %(prompt,result))
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

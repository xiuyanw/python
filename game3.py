import random
all_list=["石头","剪刀","布"]
platmon='''
(0)——石头
(1)——剪刀
(2)——布 
请输入[0/1/2]：'''
win_list=[["石头","剪刀"],["剪刀","布"],["布","石头"]]
counter_1=0
counter_2=0
while True:
    computer=random.choice(all_list)
    ind=int(input(platmon))
    if ind>2:
        print("\033[32;1merror,continue\033[0m")
        continue
    player=all_list[ind]
    if player==computer:
        print("平局")
    elif [player,computer] in win_list:
        print("you are win!!")
        counter_1+=1
        if counter_1==2:
            print("\033[31;1myou are winner\033[0m")
            break
    else:
        print("you are lose")
        counter_2+=1
        if counter_2==2:
            print("\033[32;1mgame is over,you are loser\033[0m")
            break






import random
all_choice=["石头","剪刀","布"]
win_list=[["石头","剪刀"],["剪刀",'布'],["布","石头"]]
computer=random.choice(all_choice)
prompt="""
(0)--石头
(1)--剪刀
(2)--布
请输入(0/1/2):"""
ind=int(input(prompt))
player=all_choice[ind]
print("computer choice: %s,player choice: %s" %(computer,player))
if [player,computer] in win_list:
    print("\033[31;1myou win!!\033[0m")
elif player==computer:
    print("\033[32;1m平局\033[0m")
else:
    print("\033[31;1myou lose!!\033[0m")
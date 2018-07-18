import string
import random
pass_list=[]
pass_list.extend(string.ascii_letters)
pass_list.extend(string.digits)
pass_list.extend(string.punctuation)
def randpass(n=8):
    password=''
    for i in range(n):
        password=password+random.choice(pass_list)
    return password

n=int(input("input: "))
print(randpass(n))




import random
def randpass(n=8):
    all_list=[]
    all_list.extend('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()+.,;"~{}[]|\<>?0123456789')
    pass_list=[]
    # n=int(input("please input the length of the password:"))
    password=''
    for i in range(n):
        password=random.choice(all_list)+password
    return password
    # print(password)
if __name__=='__main__':
    n = int(input("please input the length of the password:"))
    print(randpass(n))
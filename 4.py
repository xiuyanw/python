from random import randint
# def func(x):
#     return x*2+1

if __name__ == '__main__':
    alist=[randint(1,100) for i in range(10)]
    print(alist)
    result=map(lambda x:x*2+1,alist)
    print(list(result))

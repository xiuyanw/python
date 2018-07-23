from random import randint
def func1(x):
    return x%2

if __name__ == '__main__':
    alist=[randint(1,100) for i in range(10)]
    print(alist)
    result=filter(func1,alist)
    print(list(result))

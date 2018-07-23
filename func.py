import random
def func(n):


    if n == 1:
        return n
    return n*func(n-1)   #！n的算法。

if __name__ == '__main__':
    n=random.randint(1,100)
    print(func(n))
    print(func(n))
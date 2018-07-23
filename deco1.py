import random
def add(func):
    def paixu(alist=func()):

        if len(alist)<2:
            return alist
        midlle=alist[0]
        smaller=[]
        lager=[]
        for i in alist[1:]:
            if i > midlle:
                lager.append(i)
            else:
                smaller.append(i)
        return paixu(smaller) +[midlle]+paixu(lager)
    return paixu


@add
def list_1():
    alist=[random.randint(1,100) for i in range(20)]
    return alist

if __name__ == '__main__':
    print(list_1())
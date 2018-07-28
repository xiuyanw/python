import time

import threading
def sum():
    result=0
    for i in range(1,50000001):
        result+=i
    print(result)


if __name__ == '__main__':
    start=time.time()
    t1=threading.Thread(target=sum)
    t1.start()
    t2=threading.Thread(target=sum)
    t2.start()
    t1.join()
    t2.join()
    end=time.time()
    print(end-start)
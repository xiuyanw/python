import os
import time

print('hahah.....')

pid=os.fork()
if pid:
    for i in range(1,10):
        for j in range(1,i+1):
            print("%s*%s=%s " %(j,i,i*j),end='')
        print()
else:
    sum100=0

    for i in range(1,101):
        sum100+=i
    print(sum100)
    # time.sleep(1)
print('jieshu')
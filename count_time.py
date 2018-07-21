import time
import sys

for i in range(1, 11):
    print(" \r %d" % i, end='')   #原位输出覆盖。
    sys.stdout.flush()
    time.sleep(1)

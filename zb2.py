import os
import time
pid=os.fork()

if pid:
    print('In parent.sleeping....')
    print(os.waitpid(-1,1))
    time.sleep(20)
    print(os.waitpid(-1,1))
    time.sleep(60)
    print('parent done.')
else:
    print('in child.sleeping.....')
    time.sleep(15)
    print('child done.')
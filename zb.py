import os
import time
pid=os.fork()

if pid:
    print('In parent.sleeping....')
    time.sleep(60)
    print('parent done.')
else:
    print('in child.sleeping.....')
    time.sleep(15)
    print('child done.')

    #watch -n1 ps a 当子进程成为僵尸进程时，显示为Z
    #kill试图杀死僵尸进程，杀不掉，只有把父进程杀死才能干掉僵尸进程。
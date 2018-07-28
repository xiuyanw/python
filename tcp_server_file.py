import os,time
def reap():
    result=os.waitpid(-1,os.WNOHANG)
    print('Reaped child process %d' %result[0])
pid=os.fork()
if pid:
    print('In parent.Sleeping 15s...')
    time.sleep(15)
    reap()
    time.sleep(5)
    print('parent done')
else:
    print('In child.Sleeping 5s...')
    time.sleep(5)
    print('Child terinating.')
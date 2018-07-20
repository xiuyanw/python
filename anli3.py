import randpass2
import subprocess
import sys
def add_user(username,password,fname):
    data="""user infomation:
%s:%s
    """
    subprocess.call('useradd %s' % username,shell=True)
    subprocess.call(
        'echo %s | passwd --stdin %s' % (password,username),
        shell=True
    )
    with open(fname,'a') as fobj:
        fobj.write(data % (username,password))

if __name__=='__main__':
    username=sys.argv[1]
    password= randpass2.gen_pass()
    add_user(username,password,'/tmp/user.txt')
import os
import shutil
import sys
def ls(dir):
    alist=os.listdir(dir)
    if alist:
        print('%s:\n'%dir)
        print("%s\n" % alist)
    for i in alist:
        newpath=os.path.join(dir,i)
        if os.path.isdir(newpath):
            ls(newpath)
            print()

if __name__ == '__main__':
    ls(sys.argv[1])






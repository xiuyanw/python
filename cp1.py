import sys
import os
def cp(fname,dname):
    with open(fname) as src_fobj:
        if os.path.isdir(dname):
            dst_fname=os.path.join(dname,fname)
            if os.path.exists(dst_fname):
                yn=input("the %s is exists!are you sure cp(y/n)?" %dst_fname)
                if yn not in 'nN':
                    with open(dst_fname,'w') as dst_fobj:
                        for line in src_fobj:
                            dst_fobj.write(line)
            with open("%s/%s"%(dname,fname),'w') as dst_fobj:
                for line in src_fobj:
                    dst_fobj.write(line)
        else:
            if os.path.exists(dname):
                yn=input("the %s is exists!are you sure cp(y/n)?" %dname)
                if yn not in 'nN':
                    with open(dname,'w') as dst_fobj:
                        for line in src_fobj:
                            dst_fobj.write(line)
            with open(dname,'w') as dst_fobj:
                for line in src_fobj:
                    dst_fobj.write(line)
    return dst_fobj
if __name__ == '__main__':
    cp(sys.argv[1],sys.argv[2])
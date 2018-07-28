import tarfile
import os
import time
import hashlib
adict={}
def backup_fname(fname):
    week=time.strftime('%w')
    dt=time.strftime("%Y-%m-%d")
    if week==1:
        tar=tarfile.open('/tmp/%s_ful_%s.tar.gz' % (fname,dt),'w:gz')
        tar.add()

def Create_md5(fname):
    blist=[]
    alist = os.listdir(fname)
    for i in alist:
        if os.path.isdir(i):
            newpath=os.path.join(fname,i)
            blist.append(newpath)
            Create_md5(blist)
        else:
            nfile=os.path.join(fname,i)
            md5=hash_md5(nfile)
            adict[nfile]=md5
    return adict

def hash_md5(fname):
    m=hashlib.md5()
    with open(fname,'rb') as fobj:
        while True:
            data=fobj.read(4096)
            m.update(data)
            if data:
                break
    return m.hexdigest()



# for i in

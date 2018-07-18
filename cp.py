import sys
def cp(src_fname='/bin/ls',dst_fname='/root/ls'):
# src_fname='/bin/ls'
# dst_fname='/root/ls'
    src_fobj=open(src_fname,'rb')
    dst_fobj=open(dst_fname,'wb')

    while True:
        data=src_fobj.read(4096)
        if not data:
            break
        dst_fobj.write(data)

    src_fobj.close()
    dst_fobj.close()

cp(sys.argv[1],sys.argv[2])
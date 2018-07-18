astr='hello world'
alist=[10,20,30,40,50]
atuple=("bob",'tom','alice','harry')
adict={'name':'john','age':23,'like':'eat'}

for ch in astr:
    print(ch)

for i in alist:
    print(i)

for name in atuple:
    print(name)
for key in adict:
    print('%s:%s'%(key,adict[key]))

for in1 in range(1,11):
    print(in1)

for i in range(9):
    for j in range(i+1):
        print('*',end='')
    print()

for i in range(9,0,-1):
    for j in range(i):
        print('*',end='')
    print()



src_fname='/usr/bin/ls'
dst_fname='/root/ls'

src_fobj=open(src_fname,'rb')
dst_fobj=open(dst_fname,'wb')

while True:
    data=src_fobj.read(4096)
    if not data:
        break
    dst_fobj.write(data)

src_fobj.close()
dst_fobj.close()

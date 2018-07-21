import os

os.getcwd()  #当前位置,pwd
os.listdir() #ls -a

os.listdir('/tmp')  #ls /tmp
os.mkdir('/tmp/mydemo')  #mkdir
os.chdir('/tmp/mydemo')   # cd
os.mknod('test.txt')   #touch

os.symlink('/etc/hosts','zhuji')  #ln -s /etc/hosts zhuji 软链接

os.path.isfile('test.txt')   #判断test.txt是不是文件
os.path.islink('zhuji')  #判断是不是软链接

os.path.isdir('/etc/')
os.path.exists("/etc/")
os.path.basename("/tmp/abc/aaa.txt")  #取文件
'aaa.txt'
os.path.dirname("/tmp/abc/aaa.txt")   #取目录
'/tmp/abc/'

os.path.split('/tmp/abc/aaa.txt')  #切割
('/tmp/abc', 'aaa.txt')

os.path.join("/home/tom",'xyz.txt')  #拼接
'/home/tom/xyz.txt'

os.path.abspath('test.txt')  #返回绝对路径
'/tmp/mydemo/test.txt'
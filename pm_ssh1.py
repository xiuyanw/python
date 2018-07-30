import paramiko

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.1.112',username='root',password="123456")
a=ssh.exec_command('ls /abc')
print(len(a)) #a是由类文件对象组成的元组，分别是输入，输出，错误
out=a[1].read()
error=a[2].read()
print(out.decode('utf8'))
print(error.decode('utf8'))

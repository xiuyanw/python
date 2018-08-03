from collections import namedtuple
import ansible

u1=('bob',25,'bob@tedu.cn')
print(u1[0])
user=namedtuple('user',['name','age','email'])
u2=user('alice',23,'alice@tedu.cn')
print(u2[1])
print(u2[1:])
print(u2.email)
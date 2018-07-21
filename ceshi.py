import time
import pickle
dt=time.strftime('%Y-%m-%d')
print(dt)
#
# with open('/tmp/qianbao','wb') as fobj:
#     pickle.dump(10000,fobj)
#
#     number=10
# with open('/tmp/qianbao','rb') as afobj:
#     yue=pickle.load(afobj)
#     yue-=number
#     with open('/tmp/qianbao','wb') as bfobj:
#         pickle.dump(yue,bfobj)
#
# with open('/tmp/qianbao','rb') as afobj:
#     yue=pickle.load(afobj)
#     print(yue)


alist = ["时间1", "收入2", "开销", "余额", "说明"]
data = ('%-20s%-20s%-10s%-10s%-10s' % (alist[0], alist[1], alist[2], alist[3], alist[4]))
with open('/tmp/jilu', 'ab') as fobj:
    pickle.dump(data, fobj)

with open('/tmp/jilu', 'rb') as  fobj:
    while True:
        try:
            data = pickle.load(fobj)
        except EOFError:
            break
        if  data:
            print(data)

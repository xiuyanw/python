alist=[10,'john']

for ind in range(len(alist)):
    print('%s:%s'%(ind,alist[ind]))

for item in enumerate(alist):
    print('%s:%s'%(item[0],item[1]))

for ind,val in enumerate(alist):
    print('%s:%s'%(ind,val))

atuple=(81, 16, 77, 7, 71, 26, 10, 85, 66, 84)
print(sorted(atuple))
for i in reversed(atuple):
    print(i,end=',')
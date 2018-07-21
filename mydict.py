bdict=dict(['ab','cd'])

for key in bdict:
    print('%s:%s' %(key,bdict[key]))

ddict=dict([('name','bob'),('age',25)])
print(ddict)

cdict={}.fromkeys(["zhangsan",'lisi','wangwu'],11)
print(cdict)

print("%(name)s:%(age)s" % ddict)

ddict['email']= 'tom@tedu.cn'

print(ddict)
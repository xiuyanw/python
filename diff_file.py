#cp /etc/passwd .
#cp /etc/passwd  mina
#把mima改变一些,让其与passwd不一样。
#找出一个网页访问日志中的新增的网页，好做缓存。
with open('passwd') as fobj:
    aset=set(fobj)    #没有重复的了.

with open('mima') as fobj:
    bset=set(fobj)

with open("diff.txt",'w') as fobj:
    fobj.writelines(bset-aset)  #取差别，然后写到一个文本中。



import pickle
"""以前的文件写入只能写入字符串，
如果希望把任意数据对象写入文件,
取出来时数据类型不变就用到pickle了"""


"""写数据时的建脚本，要以wb的方式打开文件"""
# shop_list=["eggs",2,"peach",4,"apple"]
# with open("/tmp/shop.data",'wb') as fobj:
#     pickle.dump(shop_list,fobj)

"""读数据时的脚本，以rb的方式读取，存进去时是列表，读出来时还是列表。"""
with open('/tmp/shop.data','rb') as fobj:
    mylist=pickle.load(fobj)

print(mylist[0],mylist[1],mylist[2])
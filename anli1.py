import os

def get_fname():
    while True:
        fname = input("please input a filename: ")
        if not os.path.exists(fname):
            break
        print("%s already exists.Try again" %fname)

    return fname

def get_content():
    data_list=[]
    print("输入数据，end结束")
    while True:
        line = input(">>")
        if line == 'end':
            break
        data_list.append(line)

def wfile(fname,content):
    with open(fname,'wb') as  fobj:
        fobj.writelines(content)


if __name__=='__main__':
    fname=get_fname()
    print(fname)
    content=get_content()
    content=['%s\n' %line for line in content]
    wfile(fname,content)
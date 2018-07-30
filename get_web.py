import urllib.request
import sys
from urllib.error import HTTPError
import re
def get_web(web,fname):
    try:
        html=urllib.request.urlopen(web)
    except  HTTPError as e:
        print(e)
        if e.code==403:
            print("权限不足！！")
        elif e.code==404:
            print("没有那个地址。")
        return
    with open(fname,'wb') as fobj:
        while True:
            data=html.read(1024*4)
            if not data:
                break
            fobj.write(data)
        html.close()
if __name__ == '__main__':
    get_web(sys.argv[1],sys.argv[2])
    #保存文档为.html格式。可以用firefox+文件名打开网页.
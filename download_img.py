from get_url import get_url
from get_web import get_web
import os

get_web('http://image.baidu.com/','/tmp/baidu.html')
url=r'http://[-.\w/]+.(jpg|png|jpeg|gif)'
urls=get_url(url,'/tmp/baidu.html')
img_dir='/tmp/baidu/'
if not os.path.exists(img_dir):
    os.mkdir(img_dir)


for url in urls:
    fname=os.path.join(img_dir,url.split('/')[-1])
    try:
        get_web(url,fname)
    except :
        pass
import requests
pl={'wd':'hello word'}
r= requests.get('http://www.baidu.com/s',params=pl) #如果要传参数，通过params来传递
data = r.content
with open('/tmp/hello.html', 'wb') as fobj:
    fobj.write(data)



r1=requests.get('http://www.baidu.com')
r1.encoding='utf8'
with open('/tmp/bbdd.html','w') as fobj:
    fobj.write(r1.text)

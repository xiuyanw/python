from urllib.request import urlopen
import json
a=urlopen('http://www.weather.com.cn/data/sk/101270101.html')
data=a.read()
print(json.loads(data))
a.close()

b=urlopen('http://www.weather.com.cn/data/cityinfo/101270101.html')
data=b.read()
print(json.loads(data))
b.close()

c=urlopen('http://www.weather.com.cn/data/zs/101270101.html')
data=c.read()
print(json.loads(data))
c.close()
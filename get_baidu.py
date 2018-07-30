import requests
def get_weather():
    url='http://www.weather.com.cn/data/sk/101270101.html'
    r=requests.get(url)
    r.encoding='utf8'
    data=r.json()
    output="风向：%s,风力:%s,温度：%s,湿度：%s" %(
        data['weatherinfo']['WD'],
        data['weatherinfo']['WS'],
        data['weatherinfo']['temp'],
        data['weatherinfo']['SD'],
    )
    return output

if __name__ == '__main__':
    print(get_weather())
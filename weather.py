from urllib.request import urlopen
import json
def down_html(city_codes):
    url=urlopen('http://www.weather.com.cn/data/sk/%s.html' %city_codes)
    data=json.loads(url.read())
    output='风向：%s,风力：%s,温度：%s,湿度：%s' %(
        data['weatherinfo']['WD'],
        data['weatherinfo']['WS'],
        data['weatherinfo']['temp'],
        data['weatherinfo']['SD']
    )

    url.close()
    return output
    # b = urlopen('http://www.weather.com.cn/data/cityinfo/%s.html'%city_codes)
    # data = b.read()
    # print(json.loads(data))
    # b.close()
    #
    # c = urlopen('http://www.weather.com.cn/data/zs/%s.html'%city_codes)
    # data = c.read()
    # print(json.loads(data))
    # c.close()

def mainloop():
    prompt="""(1) 成都
(2) 龙泉译
(3) 新都
(4) 温江
(5) 金堂
(6) 双流
(7) 郫县
(8) 都江堰
(0) exit
please input your choice:"""
    city_codes={'1':101270101,'2':101270102,"3":101270103,"4":101270104,"5":101270105,"6":101270106,"7":101270107,"8":101270111}
    while True:
        choice=input(prompt).rstrip()[0]
        if choice not in '012345678':
            print("input invalid!!")
        if choice=='0':
            break
        down_html(city_codes[choice])

if __name__ == '__main__':
    mainloop()


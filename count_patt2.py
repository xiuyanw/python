from collections import Counter
import re

class Count_Patt:
    def __init__(self,fname):
        self.fname=fname

    def count_patt(self,patt):    #如果是对文件进行各种变化的操作，
        # 可以把patt从这个地方传进来，如果都是提取，只不过是对不同的文件提取，则可以把fname从这个地方传进来。
        cpatt=re.compile(patt)
        result=Counter()
        with open(self.fname) as fobj:
            for line in fobj:
                m=cpatt.search(line)
                if m:
                    result.update([m.group()])   #可以对结果进行排序
        return result

if __name__ == '__main__':
    c=Count_Patt('access_log')
    ip='^(\d+\.){3}\d+'
    a=c.count_patt(ip)
    print(a)
    print(a.most_common(3))
    br='Firefox|Chrome|MSIE'
    print(c.count_patt(br))



import re

def count_patt(fname,patt):
    cpatt = re.compile(patt)
    adict={}
    with open(fname) as fobj:
        for line in fobj:
            m=cpatt.search(line)
            if m:
                key = m.group()
                adict[key]=adict.get(key,0)+1   #字典的get方式，若果没有get到，设置返回为0
            # if key not in adict:
            #     adict[key]=1
            # else:
            #     adict[key]+=1
    return adict

if __name__ == '__main__':
    fname='access_log'
    ip='^(\d+\.){3}\d+'
    print(count_patt(fname,ip))
    br='Firefox|Chrome|MSIE'
    print(count_patt(fname,br))